#!/usr/bin/env bash
PATH_SOURCE="../text/examples/"
PATH_DESTINATION="./text"
mkdir "$PATH_DESTINATION"
find "$PATH_SOURCE" -type f -name "*.txt" -exec cp {} "$PATH_DESTINATION" \;

mapfile -t files < <(find "$PATH_SOURCE" -type f -name "*.txt")

for FILE in "${files[@]}"; do
    NAME=$(basename "$FILE" .txt)
    DIRECTORY=$(basename $(dirname "$FILE"))

    mv -f "${PATH_DESTINATION}/${NAME}.txt" "${PATH_DESTINATION}/text_examples_${DIRECTORY}_${NAME}.txt"
done
