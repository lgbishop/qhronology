#!/usr/bin/env bash

FILE_INPUT="macros.tex"
FILE_OUTPUT="macros_katex.py"

cp -rf "$FILE_INPUT" "macros.tex.txt"

# Start the MathJax configuration
echo "katex_macros = {" > "$FILE_OUTPUT"

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

        if [[ -n "$MACRO_NAME" ]]; then # Check for non-empty
            echo "  \"\\\\${MACRO_NAME//'\'}\": \"${MACRO_DEFINITION//'\'/'\\'}\"," >> "$FILE_OUTPUT"
        fi

    else
        echo "Warning: Unmatched line: $LINE" >> "$FILE_OUTPUT"  # Log unmatched lines for debugging
    fi
done

# Close the macro configuration
echo "}" >> "$FILE_OUTPUT"

echo "Conversion complete. Output written to $FILE_OUTPUT."
