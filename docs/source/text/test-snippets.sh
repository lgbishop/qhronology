#!/usr/bin/env bash
PATH_INPUT="./"
THREADS=8

touch ./test-snippets.log
echo "+--------------+" >> ./test-snippets.log
echo "| TEST RESULTS |" >> ./test-snippets.log
echo "+--------------+" >> ./test-snippets.log
echo "================================================================================" >> ./test-snippets.log

PATH_SNIPPETS="./snippets"
rm -rf "$PATH_SNIPPETS"
mkdir -p "$PATH_SNIPPETS"

rm -f ./jobs-rst.txt
for f in $(find "$PATH_INPUT" -type f -name "*.rst"); do
    echo "$f" >> ./jobs-rst.txt
done

mapfile -t jobs < ./jobs-rst.txt

echo "+------------+"
echo "| TEST START |"
echo "+------------+"

for FILE in "${jobs[@]}"; do
    NAME=$(basename $FILE) # Remove directories
    NAME="${NAME%.*}" # Remove extension

    echo ">>> import sympy as sp" >> "${PATH_SNIPPETS}/${NAME}.txt"
    echo ">>> import numpy as np" >> "${PATH_SNIPPETS}/${NAME}.txt"

    awk -v PATH_OUT="$PATH_SNIPPETS" -v NAME="$NAME" '
      function strip_leading_ws(s){ sub(/^[[:space:]]+/, "", s); return s }

      /^[[:space:]]*\.\.[[:space:]]*code::[[:space:]]*/ {
        count++
        out = PATH_OUT "/" NAME ".txt." count
        printing = 1
        next
      }

      /^[[:space:]]*\.\.[[:space:]]*literalinclude::[[:space:]]*/ {
        count++
        out = PATH_OUT "/" NAME ".txt." count

        line = $0
        sub(/^[[:space:]]*\.\.[[:space:]]*literalinclude::[[:space:]]*/, "", line)
        line = strip_leading_ws(line)

        n = line
        sub(/.*\//, "", n)

        if (n ~ /\.py[[:space:]]*$/) {
          sub(/\.py[[:space:]]*$/, "", n)
          print ">>> from " n " import *"
          print ">>> from " n " import *" > out
        }

        printing = 0
        next
      }

      printing && /^[[:space:]]*$/ { next }

      printing && /^[[:space:]]*\.\.[[:space:]]*[^[:space:]]+::/ {
        printing = 0
        next
      }

      printing {
        if (index($0, ".diagram")) $0 = $0 "  # doctest: +SKIP"
        sub(/^[[:space:]]+/, "", $0)
        if (index($0, "from ") == 1) $0 = ">>> " $0
        if (index($0, "import ") == 1) $0 = ">>> " $0
        if (index($0, "Duration:")) $0 = $0 "  # doctest: +SKIP"
        if (index($0, "The function:")) $0 = $0 "  # doctest: +SKIP"
        if (index($0, "The Deutsch-Jozsa result:")) $0 = $0 "  # doctest: +SKIP"
        print $0
        print > out
      }
    ' "$FILE" >> "${PATH_SNIPPETS}/${NAME}.txt"
    find "$PATH_SNIPPETS" -type f -name "${NAME}.txt.*" -delete

done

for f in $(find "./examples" -type f -name "*.py"); do
    cp "$f" "$PATH_SNIPPETS"
    NAME=$(basename $f)  # Remove directories
    NAME="${NAME%.*}"  # Remove extension
    sed -i '/\.diagram(/d' "${PATH_SNIPPETS}/${NAME}.py"
    # sed -i '/\.print(/d' "${PATH_SNIPPETS}/${NAME}.py"
    # sed -i '/print(/d' "${PATH_SNIPPETS}/${NAME}.py"

    sed -n '1,/\# Results/p' "${PATH_SNIPPETS}/${NAME}.py" > "${PATH_SNIPPETS}/${NAME}.py.preresults"
    sed -n '/\# Results/,$p' "${PATH_SNIPPETS}/${NAME}.py" > "${PATH_SNIPPETS}/${NAME}.py.postresults"

    sed -i 's/^/    /' "${PATH_SNIPPETS}/${NAME}.py.postresults"
    sed -i '1s/^/    print\(\"\"\)\n/' "${PATH_SNIPPETS}/${NAME}.py.postresults"
    sed -i '1s/^/def main\(\)\:\n/' "${PATH_SNIPPETS}/${NAME}.py.postresults"
    echo "" >> "${PATH_SNIPPETS}/${NAME}.py.postresults"
    echo "if __name__ == '__main__':" >> "${PATH_SNIPPETS}/${NAME}.py.postresults"
    echo "    main()" >> "${PATH_SNIPPETS}/${NAME}.py.postresults"

    cat "${PATH_SNIPPETS}/${NAME}.py.preresults" "${PATH_SNIPPETS}/${NAME}.py.postresults" > "${PATH_SNIPPETS}/${NAME}.py"

done

rm -f ./jobs-snippets.txt
for f in $(find "$PATH_SNIPPETS" -type f -name "*.txt"); do
    echo "$f" >> ./jobs-snippets.txt
done

mapfile -t jobs < ./jobs-snippets.txt

for FILE in "${jobs[@]}"; do
    (
    NAME=$(basename $FILE)  # Remove directories
    NAME="${NAME%.*}"  # Remove extension

    PYTHONPATH="$PYTHONPATH:$(pwd)/../../../../qhronology/src/:$PATH_SNIPPETS" /run/current-system/sw/bin/python -B -m doctest -o NORMALIZE_WHITESPACE -v "${PATH_SNIPPETS}/${NAME}.txt" > "${PATH_SNIPPETS}/${NAME}.test" 2>&1

    if grep -q "Test passed\." "${PATH_SNIPPETS}/${NAME}.test"; then
        echo "PASSED: ${NAME}"
    else
        echo "FAILED: ${NAME}"
        cat "${PATH_SNIPPETS}/${NAME}.test"
    fi

    ) &

    if (( $(jobs -p | wc -w) == $THREADS )); then
        wait -n
    fi
done
wait

FAILED=0
for FILE in "${jobs[@]}"; do
    NAME=$(basename $FILE)  # Remove directories
    NAME="${NAME%.*}"  # Remove extension
    if grep -q "Test passed\." "${PATH_SNIPPETS}/${NAME}.test"; then
        echo "PASSED: ${NAME}" >> ./test-snippets.log
    else
        FAILED=$((FAILED+1))
        echo "FAILED: ${NAME}" >> ./test-snippets.log
        echo "================================================================================" >> ./test-snippets.log
        cat "${PATH_SNIPPETS}/${NAME}.test" >> ./test-snippets.log
        echo "================================================================================" >> ./test-snippets.log
    fi
done

echo "================================================================================" >> ./test-snippets.log
echo "Failed: ${FAILED}" >> ./test-snippets.log

rm -f ./jobs-rst.txt
rm -rf "$PATH_SNIPPETS"

rm -f ./jobs-snippets.txt
cat ./test-snippets.log
rm -f ./test-snippets.log
