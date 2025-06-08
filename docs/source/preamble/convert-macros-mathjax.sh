#!/usr/bin/env bash

FILE_INPUT="macros.tex"
FILE_OUTPUT="macros_mathjax.py"

cp -rf "$FILE_INPUT" "macros.tex.txt"

# Start the MathJax configuration
echo "mathjax3_config = {" > "$FILE_OUTPUT"
echo "  \"tex\": {" >> "$FILE_OUTPUT"
echo "    \"macros\": {" >> "$FILE_OUTPUT"

# Read the input file into an array
mapfile -t lines < "$FILE_INPUT"

# Loop over the array
for LINE in "${lines[@]}"; do
    # Skip empty lines and comments
    if [[ -z "$LINE" || "$LINE" =~ ^% ]]; then
        continue
    fi

    # Use Perl to match and extract the macro components
    if echo "$LINE" | perl -n -e 'if (/^(\\(?:newcommand|renewcommand|def))\s*{(\\?[a-zA-Z]+)}\s*(?:\[(\d+)\])?\s*{(.*)}/) { print "$1,$2,$3,$4\n"; }' ; then
        # Extracted values
        IFS=',' read -r MACRO_TYPE MACRO_NAME MACRO_NUMBER MACRO_DEFINITION <<< "$(echo "$LINE" | perl -n -e 'if (/^(\\(?:newcommand|renewcommand|def))\s*{(\\?[a-zA-Z]+)}\s*(?:\[(\d+)\])?\s*{(.*)}/) { print "$1,$2,$3,$4\n"; }')"

        if [[ -n "$MACRO_NAME" ]]; then # check for non-empty
            if [[ -n "$MACRO_NUMBER" ]]; then
                echo "      \"${MACRO_NAME//'\'}\": [\"{${MACRO_DEFINITION//'\'/'\\'}}\", $MACRO_NUMBER]," >> "$FILE_OUTPUT"
            else
                echo "      \"${MACRO_NAME//'\'}\": \"{${MACRO_DEFINITION//'\'/'\\'}}\"," >> "$FILE_OUTPUT"
            fi
        fi
    else
        echo "Warning: Unmatched line: $LINE" >> "$FILE_OUTPUT"  # Log unmatched lines for debugging
    fi
done

# Close the MathJax configuration
echo "    }" >> "$FILE_OUTPUT"
echo "  }" >> "$FILE_OUTPUT"
echo "}" >> "$FILE_OUTPUT"

echo "Conversion complete. Output written to $FILE_OUTPUT."
