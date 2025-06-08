#!/usr/bin/env bash

# set -ex

############################################################
# Help                                                     #
############################################################
Help()
{
  echo 'This bash script is used to create Qhronology'\''s static artwork.'
  echo
  echo 'Usage: bash static.sh [options]'
  echo
  echo 'Options:'
  echo '-h, --help             Print this help.'
  echo '-i, --input            Input TeX file (without extension) to process. Defaults to "logo-main-bold".'
  echo '-o, --output           Filename to be given to the output. Defaults to "$(basename "$0" ".sh")" (i.e., the name of the script used to call this script).'
  echo '-d, --directory        Path of the directory in which to place the output. Defaults to "$(pwd)/output".'
  echo '-O, --options          Options to be passed to the LaTeX renderer. Not currently implemented.'
  echo '-F, --format           File extension(s) of the file output format target(s), given as a concatenated string. Defaults to "webp". Currently only supports distinguishing of "pdf" output, for single-frame vector graphics purposes.'
  echo '-E, --engine           Names of LaTeX engine to use. Can be either "xelatex" or "pdflatex". Defaults to "pdflatex".'
  echo '-T, --themes           Name of themes to render. Currently can be "" or "both". Defaults to "both". In future, will be able to use comma-delimited string containing "light" and "dark".'
  echo '-c, --clean            Boolean value specifying whether to clean the output directory (i.e., remove all rendered frames, leaving just the final image or animation). Defaults to `false`.'
  echo '-H, --horizontal       The horizontal resolution, given as an integer. Defaults to `2000`.'
  echo '-V, --vertical         The vertical resolution, given as an integer. Defaults to ''.'
  echo '-q, --quality          The value passed to the `-quality` option of the final output'\''s compression. Defaults to `60`.'
}

############################################################
# Options                                                  #
############################################################

# Set defaults
FILE_INPUT="logo-text-bold"
PATH_OUTPUT="$(pwd)/output"
FILE_OUTPUT=$(basename "$0" ".sh")
OPTIONS=""
FORMAT="png"
ENGINE="pdflatex"
THEMES="both"
CLEAN=true
RESOLUTION_HORIZONTAL=2000
RESOLUTION_VERTICAL=''
QUALITY=64

# Get the options
POSITIONAL_ARGS=()

while [[ $# -gt 0 ]]; do
  case $1 in
    -h|--help)
      Help
      exit
      ;;
    -i|--input)
      FILE_INPUT="$2"
      shift # past argument
      shift # past value
      ;;
    -o|--output)
      FILE_OUTPUT="$2"
      shift # past argument
      shift # past value
      ;;
    -d|--directory)
      PATH_OUTPUT="$2"
      shift # past argument
      shift # past value
      ;;
    -O|--options)
      OPTIONS="$2"
      shift # past argument
      shift # past value
      ;;
    -F|--format)
      FORMAT="$2"
      shift # past argument
      shift # past value
      ;;
    -E|--engine)
      ENGINE="$2"
      shift # past argument
      shift # past value
      ;;
    -T|--themes)
      THEMES="$2"
      shift # past argument
      shift # past value
      ;;
    -c|--clean)
      CLEAN="$2"
      shift # past argument
      shift # past value
      ;;
    -H|-horizontal)
      RESOLUTION_HORIZONTAL="$2"
      shift # past argument
      shift # past value
      ;;
    -V|--vertical)
      RESOLUTION_VERTICAL="$2"
      shift # past argument
      shift # past value
      ;;
    -q|--quality)
      QUALITY="$2"
      shift # past argument
      shift # past value
      ;;
    -*|--*)
      echo "Unknown option $1."
      exit 1
      ;;
    *)
      POSITIONAL_ARGS+=("$1") # save positional arg
      shift # past argument
      ;;
  esac
done

set -- "${POSITIONAL_ARGS[@]}" # restore positional parameters

mkdir -p $PATH_OUTPUT
PATH_SCRIPTS=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PATH_LATEX=$(dirname $PATH_SCRIPTS)"/latex"

cd $PATH_LATEX

if [[ $ENGINE == "xelatex" ]]; then
    xelatex -shell-escape -synctex=0 -interaction=batchmode -file-line-error -jobname="${FILE_OUTPUT}-uncropped" -output-directory="$PATH_OUTPUT" "${PATH_LATEX}/${FILE_INPUT}.tex"
else
    pdflatex -shell-escape -synctex=0 -interaction=batchmode -file-line-error -jobname="${FILE_OUTPUT}-uncropped" -output-directory="$PATH_OUTPUT" "${PATH_LATEX}/${FILE_INPUT}.tex"
fi

pdfcrop "${PATH_OUTPUT}/${FILE_OUTPUT}-uncropped.pdf" "${PATH_OUTPUT}/${FILE_OUTPUT}.pdf" # Use this instead of relying on the `standalone` package's cropping functionality - it doesn not always work properly
magick -density 4000 "${PATH_OUTPUT}/${FILE_OUTPUT}.pdf" -quality $QUALITY% -resize "$RESOLUTION_HORIZONTAL"x"$RESOLUTION_VERTICAL" "${PATH_OUTPUT}/${FILE_OUTPUT}.png"

if [[ $FORMAT == *"svg"* ]]; then
    pdf2svg "${PATH_OUTPUT}/${FILE_OUTPUT}.pdf" "${PATH_OUTPUT}/${FILE_OUTPUT}.svg"
    if [[ $THEMES == *"both"* ]]; then
        cp -f "${PATH_OUTPUT}/${FILE_OUTPUT}.svg" "${PATH_OUTPUT}/${FILE_OUTPUT}-alt.svg"
        perl -i -pe 's/rgb\((.*?)%, (.*?)%, (.*?)%\)/"rgb(" . (100 - $1) . "%, " . (100 - $2) . "%, " . (100 - $3) . "%)"/ge' "${PATH_OUTPUT}/${FILE_OUTPUT}-alt.svg" # Invert colours
        perl -i -pe 's/rgb\((.*?)%, (.*?)%, (.*?)%\)/"rgb( 100%, 100%, 100%)"/ge' "${PATH_OUTPUT}/${FILE_OUTPUT}-alt.svg" # Make all colours white
    fi
fi

rm -f "${PATH_OUTPUT}/${FILE_OUTPUT}-uncropped.aux"
rm -f "${PATH_OUTPUT}/${FILE_OUTPUT}-uncropped.log"

if [[ $CLEAN == true ]]; then
    if [[ $FORMAT != *"pdf"* ]]; then
        rm -f "${PATH_OUTPUT}/${FILE_OUTPUT}.pdf"
    fi
    rm -f "${PATH_OUTPUT}/${FILE_OUTPUT}-uncropped.pdf"
fi
