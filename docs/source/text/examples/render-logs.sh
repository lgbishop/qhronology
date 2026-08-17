#!/usr/bin/env bash
PATH_INPUT="./"
THREADS=8

rm -f ./jobs-examples.txt
for f in $(find "$PATH_INPUT" -type f -name "*.py"); do
    echo "$f" >> ./jobs-examples.txt
done

# For when you want to test only specific files:
# rm -f ./jobs-examples.txt
# touch ./jobs-examples.txt
# echo "./algorithms/tomography_weak.py" >> ./jobs-examples.txt

mapfile -t jobs < ./jobs-examples.txt

for FILE in "${jobs[@]}"; do
    (
    # FILENAME="${FILENAME##*/}" # Remove parent directories
    NAME=$(basename $FILE)
    NAME="${NAME%.*}" # Remove extension
    PATH_RELATIVE=$(dirname $FILE) # Get the directory of the file
    PATH_ABSOLUTE=$(realpath $FILE)

    echo "${PATH_ABSOLUTE%.*}"

    PYTHONPATH="$PYTHONPATH:$(pwd)/../../../../../qhronology/src/" /run/current-system/sw/bin/python -B "${PATH_ABSOLUTE%.*}.py" > "${PATH_RELATIVE}/${NAME}.log" 2>&1

    cat "${PATH_RELATIVE}/${NAME}.log"

    ) &

    if (( $(jobs -p | wc -w) == $THREADS )); then
        wait -n
    fi
done
wait

rm -f ./jobs-examples.txt
