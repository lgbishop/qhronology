#!/usr/bin/env bash
PATH_INPUT="./"
THREADS=8

touch ./test-report.log
echo "+--------------+" >> ./test-report.log
echo "| TEST RESULTS |" >> ./test-report.log
echo "+--------------+" >> ./test-report.log
echo "================================================================================" >> ./test-report.log

rm -f ./jobs-examples.txt
for f in $(find "$PATH_INPUT" -type f -name "*.py"); do
    echo "$f" >> ./jobs-examples.txt
done

mapfile -t jobs < ./jobs-examples.txt

for FILE in "${jobs[@]}"; do
    (
    # FILENAME="${FILENAME##*/}" # Remove parent directories
    NAME=$(basename $FILE)
    NAME="${NAME%.*}" # Remove extension
    PATH_RELATIVE=$(dirname $FILE) # Get the directory of the file
    PATH_ABSOLUTE=$(realpath $FILE)

    echo "${PATH_ABSOLUTE%.*}"

    PYTHONPATH="$PYTHONPATH:$(pwd)/../../../../../qhronology/src/" /run/current-system/sw/bin/python -B "${PATH_ABSOLUTE%.*}.py" > "${PATH_RELATIVE}/${NAME}.test" 2>&1

    cat "${PATH_RELATIVE}/${NAME}.test"

    echo "================================================================================"

    diff --text "${PATH_RELATIVE}/${NAME}.test" "${PATH_RELATIVE}/${NAME}.log" > "${PATH_RELATIVE}/${NAME}.diff"

    if [ -s "${PATH_RELATIVE}/${NAME}.diff" ]; then # Check if .diff file is empty
        touch "${PATH_RELATIVE}/${NAME}.result"
        echo "${PATH_RELATIVE}/${NAME}.py:" >> "${PATH_RELATIVE}/${NAME}.result"
        cat "${PATH_RELATIVE}/${NAME}.diff" >> "${PATH_RELATIVE}/${NAME}.result"
        echo "================================================================================" >> "${PATH_RELATIVE}/${NAME}.result"
        cat "${PATH_RELATIVE}/${NAME}.result" >> ./test-report.log
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
cat ./test-report.log
rm -f ./test-report.log
