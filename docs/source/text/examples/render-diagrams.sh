#!/usr/bin/env bash
PATH_INPUT="./"
THREADS=8

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

    # BREAK="Output"
    BREAK=".diagram"
    SCRIPT="${PATH_RELATIVE}/${NAME}-truncated.py"

    touch "$SCRIPT"

    # Read the entire file into an array
    mapfile -t LINES < "$FILE"

    # Find the last occurrence of BREAK
    INDEX_LAST=-1
    for i in "${!LINES[@]}"; do
        if [[ "${LINES[i]}" == *"$BREAK"* ]]; then
            INDEX_LAST=$i
        fi
    done

    # If a BREAK was found, write lines up to and including the last BREAK to SCRIPT
    if [ $INDEX_LAST -ne -1 ]; then
        for ((i=0; i<=INDEX_LAST; i++)); do
            echo "${LINES[i]}" >> "$SCRIPT"
        done
    fi

    echo "${PATH_ABSOLUTE%.*}-truncated.py"

    cat "$SCRIPT"

    PYTHONPATH="$PYTHONPATH:/home/lachie/Dropbox/programming/python/qhronology/src/" /run/current-system/sw/bin/python -B "${PATH_ABSOLUTE%.*}-truncated.py" > "${PATH_RELATIVE}/${NAME}.txt" 2>&1
    rm -f "$SCRIPT"

    ) &

    if (( $(jobs -p | wc -w) == $THREADS )); then
        wait -n
    fi
done
wait

rm -f ./jobs-examples.txt
