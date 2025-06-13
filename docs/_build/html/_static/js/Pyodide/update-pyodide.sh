# Acquire the latest Pyodide release and put it in the correct place.

rm -rf ./pyodide

# curl -OL https://github.com/pyodide/pyodide/releases/download/0.27.7/pyodide-0.27.7.tar.bz2
bzip2 -dk pyodide-*.tar.bz2
tar -xvf pyodide-*.tar

mv -f ./pyodide ./pyodide-temp
mkdir ./pyodide

mv -f ./pyodide-temp/pyodide.js ./pyodide
mv -f ./pyodide-temp/pyodide.mjs ./pyodide
mv -f ./pyodide-temp/pyodide.js.map ./pyodide
mv -f ./pyodide-temp/pyodide.mjs.map ./pyodide
mv -f ./pyodide-temp/sympy-*.whl ./pyodide
mv -f ./pyodide-temp/sympy-*.metadata ./pyodide
mv -f ./pyodide-temp/mpmath-*.whl ./pyodide
mv -f ./pyodide-temp/mpmath-*.metadata ./pyodide
mv -f ./pyodide-temp/numpy-*.whl ./pyodide
mv -f ./pyodide-temp/numpy-*.metadata ./pyodide
mv -f ./pyodide-temp/micropip-*.whl ./pyodide
mv -f ./pyodide-temp/micropip-*.metadata ./pyodide
mv -f ./pyodide-temp/packaging-*.whl ./pyodide
mv -f ./pyodide-temp/packaging-*.metadata ./pyodide
mv -f ./pyodide-temp/pyodide.asm.wasm ./pyodide
mv -f ./pyodide-temp/python_stdlib.zip ./pyodide
mv -f ./pyodide-temp/pyodide.asm.js ./pyodide
mv -f ./pyodide-temp/pyodide-lock.json ./pyodide

rm -rf ./pyodide-temp

curl -OL https://github.com/lgbishop/qhronology/releases/download/1.0.0/qhronology-1.0.0-py3-none-any.whl
mv -f qhronology-*.whl ./pyodide

rm -rf pyodide-*.tar.bz2
rm -rf pyodide-*.tar

# https://pyodide.org/en/stable/usage/downloading-and-deploying.html#github-releases
