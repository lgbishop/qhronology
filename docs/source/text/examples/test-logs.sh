#!/usr/bin/env bash
PATH_INPUT="./"
THREADS=8

touch ./test-logs.log
echo "+--------------+" >> ./test-logs.log
echo "| TEST RESULTS |" >> ./test-logs.log
echo "+--------------+" >> ./test-logs.log
echo "================================================================================" >> ./test-logs.log

rm -f ./jobs-examples.txt
for f in $(find "$PATH_INPUT" -type f -name "*.py"); do
    echo "$f" >> ./jobs-examples.txt
done

mapfile -t jobs < ./jobs-examples.txt

echo "+------------+"
echo "| TEST START |"
echo "+------------+"

for FILE in "${jobs[@]}"; do
    (
    NAME=$(basename $FILE)  # Remove parent directories
    NAME="${NAME%.*}"  # Remove extension
    PATH_RELATIVE=$(dirname $FILE)
    PATH_ABSOLUTE=$(realpath $FILE)

    echo "${PATH_ABSOLUTE%.*}"

    PYTHONPATH="$PYTHONPATH:$(pwd)/../../../../../qhronology/src/" /run/current-system/sw/bin/python -B "${PATH_ABSOLUTE%.*}.py" > "${PATH_RELATIVE}/${NAME}.test" 2>&1

    cat "${PATH_RELATIVE}/${NAME}.test"

    echo "================================================================================"

    diff --text "${PATH_RELATIVE}/${NAME}.test" "${PATH_RELATIVE}/${NAME}.log" > "${PATH_RELATIVE}/${NAME}.diff"

    if [ -s "${PATH_RELATIVE}/${NAME}.diff" ]; then  # Check if .diff file is empty
        touch "${PATH_RELATIVE}/${NAME}.result"
        echo "${PATH_RELATIVE}/${NAME}.py:" >> "${PATH_RELATIVE}/${NAME}.result"
        cat "${PATH_RELATIVE}/${NAME}.diff" >> "${PATH_RELATIVE}/${NAME}.result"
        echo "================================================================================" >> "${PATH_RELATIVE}/${NAME}.result"
        cat "${PATH_RELATIVE}/${NAME}.result" >> ./test-logs.log
    fi

    rm -f "${PATH_RELATIVE}/${NAME}.test"
    rm -f "${PATH_RELATIVE}/${NAME}.diff"
    rm -f "${PATH_RELATIVE}/${NAME}.result"

    ) &

    if (( $(jobs -p | wc -w) == $THREADS )); then
        wait -n
    fi
done
wait

rm -f ./jobs-examples.txt
cat ./test-logs.log
rm -f ./test-logs.log
