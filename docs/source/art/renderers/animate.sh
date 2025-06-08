#!/usr/bin/env bash

# This bash script is used to create Qhronology's fancy logo, both the static and animated versions.

# Dependencies include:
# - `pdflatex` [texlive] (for vector art)
# - `pdfcrop` [texlive] (for cropping where LaTeX's `standalone` class/package is unable to do so proper)
# - `magick` [imagemagick]
# - `pdfimages` [poppler_utils]
# - `composite` [imagemagick] (for conversion and image effects),
# - `seq` [coreutils] (for looping),
# - `webpmux` [libwebp] (for generating the animated WebP).
# A full TeX Live environment (including ghostscript for vector rasterization) is also required for generating the intermediate PDF (and raster) output assets.

# All assets are generated from the two LaTeX files:
# 1. "clock.tex",
# 2. "$FILE_INPUT.tex". For example, one of the provided files of the form `logo-*.tex` or `icon-*.tex`.
# Both of these files must reside in the directory `./latex` relative to where this script is called.

# A pre-existing logo file, e.g., `logo-text-bold-light.pdf`, is required if a logo is desired in the final composition.
# An appropriate logo file can be created using the accompanying script `static.sh`.

# See the file `logo-main-50fps-3sec.sh` in the repository for an example of usage.

# set -ex

############################################################
# Help                                                     #
############################################################
Help()
{
  echo 'This bash script is used to create Qhronology'\''s animated logo.'
  echo
  echo 'Usage: bash animate.sh [options]'
  echo
  echo 'Options:'
  echo '-h, --help             Print this help.'
  echo '-i, --input            Input TeX file (without extension) to process. Defaults to "logo-main".'
  echo '-o, --output           Filename to be given to the output. Defaults to "$(basename "$0" ".sh")" (i.e., the name of the script used to call this script).'
  echo '-d, --directory        Path of the directory in which to place the output. Defaults to "$(pwd)/output".'
  echo '-F, --format           File extension(s) of the file output format target(s), given as a concatenated string. Defaults to "webp". Currently only supports distinguishing of "pdf" output, for single-frame vector graphics purposes.'
  echo '-e, --exclude          Names of features (currently only "clock" and "wormhole"), given as concatenated strings, to be excluded in the composition of the output. Defaults to "" (empty string).'
  echo '-l, --logo             Path to the PDF file to be used as the logo. Defaults to "" (empty string, which thus omits the logo from the output).'
  echo '-c, --clean            Boolean value specifying whether to clean the output directory (i.e., remove all rendered frames, leaving just the final image or animation). Defaults to `false`.'
  echo '-t, --threads          Number of parallel process workers to spawn in the frame-render loop. Defaults to `1`.'
  echo '-f, --frame-rate       Frame rate (per second) of the animation. Defaults to `50`.'
  echo '-p, --period           Period (in seconds) of the animation. Defaults to `3`.'
  echo '-n, --number           Number of frames to calculate. Defaults to the frame rate multiplied by the period (i.e., all necessary frames for the entire loop).'
  echo '-g, --gravity          The value passed to the `-gravity` option of the composition'\''s `magick` command. Used as an anchor point for cropping the output. Defaults to "Center".'
  echo '-a, --aspect           The aspect ratio of the output, given as a string of two colon-delimited integers. Defaults to "4:1".'
  echo '-w, --width            The horizontal resolution of the output as an integer. Defaults to `4000`.'
  echo '-A, --alpha            Boolean value specifying whether to have transparent backgrounds in the non-PDF output. Defaults to `false`.'
  echo '-r, --resize           The horizontal resolution to which the final output will be resized. Defaults to `720`.'
  echo '-q, --quality          The value passed to the `-quality` option of the final output'\''s compression. Defaults to `60`.'
  echo '-C, --circles          The number of circles of the wormhole. Defaults to `45`.'
  echo '-S, --sectors          The number of sectors of the wormhole. Defaults to `30`.'
  echo '-R, --rotations        The number of rotations of the wormhole within the the animation'\''s period. Defaults to `2`.'
  echo '-D, --clock-distort    Name of the custom animated distortion effect to apply to the clock. One of "static", "swimming", or "floating". Defaults to "static".'
  echo '-B, --clock-blur       Boolean value specifying whether to apply a motion-blur effect the fringes of the clock. Defaults to `false`.'
  echo '-E, --clock-edge       The width of the clock'\''s edge in pixels. Defaults to `4.25`.'
  echo '-T, --time             The initial time displayed on the clock, given as a string of three colon-delimited ordered integers (i.e., "h:m:s"). Defaults to "3:53:7".'
  echo '-H, --hands            The number of complete clockwise revolutions of the clock hands within the animation'\''s period, given as a string of three colon-delimited ordered integers (i.e. "h:m:s"). Negative integers yield anti-clockwise revolutions. Defaults to "-1:2:-3".'
  echo '-v, --cycles           The number of complete horizontal and vertical cycles of the clock'\''s "floating" motion within the animation'\''s period, given as a string of two comma-delimited ordered integers (i.e., "h,v"). Defaults to "1,1".'
  echo '-V, --amplitudes       The amplitude of the horizontal and vertical cycles of the clock'\''s "floating" motion within the animation'\''s period, given as a string of two comma-delimited ordered integers (i.e., "h,v"). Defaults to "1,1".'
}

############################################################
# Options                                                  #
############################################################

# Set defaults.
FILE_INPUT="logo-main"
PATH_OUTPUT="$(pwd)/output"
FILE_OUTPUT="$(basename "$0" ".sh")"
FORMAT="webp"
EXCLUDE=""
LOGO=""
CLEAN=true
THREADS=1
FPS=50
PERIOD=3
GRAVITY="Center"
ASPECT_RATIO="4:1"
RESOLUTION_HORIZONTAL=4000
TRANSPARENCY=false
RESIZE=720
QUALITY=60

WORMHOLE_CIRCLES=45
WORMHOLE_SECTORS=30
WORMHOLE_ROTATIONS=2

CLOCK_DISTORT="static"
CLOCK_BLUR=false
CLOCK_EDGE_WIDTH=4.25
CLOCK_HAND_INITIAL_HOUR=3
CLOCK_HAND_INITIAL_MINUTE=53
CLOCK_HAND_INITIAL_SECOND=7
CLOCK_HAND_REVOLUTIONS_HOUR=-1
CLOCK_HAND_REVOLUTIONS_MINUTE=2
CLOCK_HAND_REVOLUTIONS_SECOND=-3
CLOCK_POSITION_CYCLES_HORIZONTAL=1
CLOCK_POSITION_CYCLES_VERTICAL=1
CLOCK_POSITION_AMPLITUDE_HORIZONTAL=1
CLOCK_POSITION_AMPLITUDE_VERTICAL=1

# Get the options.
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
    -F|--format)
      FORMAT="$2"
      shift # past argument
      shift # past value
      ;;
    -e|--exclude)
      EXCLUDE="$2"
      shift # past argument
      shift # past value
      ;;
    -l|--logo)
      LOGO="$2"
      shift # past argument
      shift # past value
      ;;
    -c|--clean)
      CLEAN="$2"
      shift # past argument
      shift # past value
      ;;
    -t|--threads)
      THREADS="$2"
      shift # past argument
      shift # past value
      ;;
    -f|--frame-rate)
      FPS="$2"
      shift # past argument
      shift # past value
      ;;
    -p|--period)
      PERIOD="$2"
      shift # past argument
      shift # past value
      ;;
    -n|--number)
      FRAMES_REQUESTED="$2"
      shift # past argument
      shift # past value
      ;;
    -g|--gravity)
      GRAVITY="$2"
      shift # past argument
      shift # past value
      ;;
    -a|--aspect)
      ASPECT_RATIO="$2"
      shift # past argument
      shift # past value
      ;;
    -w|--width)
      RESOLUTION_HORIZONTAL="$2"
      shift # past argument
      shift # past value
      ;;
    -A|--alpha)
      TRANSPARENCY="$2"
      shift # past argument
      shift # past value
      ;;
    -r|--resize)
      RESIZE="$2"
      shift # past argument
      shift # past value
      ;;
    -q|--quality)
      QUALITY="$2"
      shift # past argument
      shift # past value
      ;;
    -C|--circles)
      WORMHOLE_CIRCLES="$2"
      shift # past argument
      shift # past value
      ;;
    -S|--sectors)
      WORMHOLE_SECTORS="$2"
      shift # past argument
      shift # past value
      ;;
    -R|--rotations)
      WORMHOLE_ROTATIONS="$2"
      shift # past argument
      shift # past value
      ;;
    -D|--clock-distort)
      CLOCK_DISTORT="$2"
      shift # past argument
      shift # past value
      ;;
    -B|--clock-blur)
      CLOCK_BLUR="$2"
      shift # past argument
      shift # past value
      ;;
    -E|--clock-edge)
      CLOCK_EDGE_WIDTH="$2"
      shift # past argument
      shift # past value
      ;;
    -T|--time)
      TIME_DELIMITED="$2"
      TIME_ARRAY=(${TIME_DELIMITED//:/ })
      CLOCK_HAND_INITIAL_HOUR=${TIME_ARRAY[0]}
      CLOCK_HAND_INITIAL_MINUTE=${TIME_ARRAY[1]}
      CLOCK_HAND_INITIAL_SECOND=${TIME_ARRAY[2]}
      shift # past argument
      shift # past value
      ;;
    -H|--hands)
      CLOCK_HAND_REVOLUTIONS="$2"
      CLOCK_HAND_REVOLUTIONS_ARRAY=(${CLOCK_HAND_REVOLUTIONS//:/ })
      CLOCK_HAND_REVOLUTIONS_HOUR=${CLOCK_HAND_REVOLUTIONS_ARRAY[0]}
      CLOCK_HAND_REVOLUTIONS_MINUTE=${CLOCK_HAND_REVOLUTIONS_ARRAY[1]}
      CLOCK_HAND_REVOLUTIONS_SECOND=${CLOCK_HAND_REVOLUTIONS_ARRAY[2]}
      shift # past argument
      shift # past value
      ;;
    -v|--cycles)
      CLOCK_POSITION_CYCLES="$2"
      CLOCK_POSITION_CYCLES_ARRAY=(${CLOCK_POSITION_CYCLES//,/ })
      CLOCK_POSITION_CYCLES_HORIZONTAL=${CLOCK_POSITION_CYCLES_ARRAY[0]}
      CLOCK_POSITION_CYCLES_VERTICAL=${CLOCK_POSITION_CYCLES_ARRAY[1]}
      shift # past argument
      shift # past value
      ;;
    -V|--amplitudes)
      CLOCK_POSITION_AMPLITUDE="$2"
      CLOCK_POSITION_AMPLITUDE_ARRAY=(${CLOCK_POSITION_AMPLITUDE//,/ })
      CLOCK_POSITION_AMPLITUDE_HORIZONTAL=${CLOCK_POSITION_AMPLITUDE_ARRAY[0]}
      CLOCK_POSITION_AMPLITUDE_VERTICAL=${CLOCK_POSITION_AMPLITUDE_ARRAY[1]}
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

if [[ $FORMAT == "pdf" ]]; then
    FRAMES_TOTAL=1
else
    FRAMES_TOTAL=$((FPS * PERIOD))
fi

FRAMES_REQUESTED="${FRAMES_REQUESTED:-$FRAMES_TOTAL}"
mkdir -p $PATH_OUTPUT
CWD=$(pwd)
PATH_CALLED=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PATH_LATEX=$(dirname $PATH_CALLED)"/scripts/../latex"

############################################################
# Main                                                     #
############################################################

(
for FRAMES_CURRENT in $(seq 0 $((FRAMES_REQUESTED - 1))); do
    (
    echo $FRAMES_CURRENT
    echo $FPS
    echo $PERIOD

    PATH_TEMP=$(mktemp -d '/tmp/render-XXXXXXXXXX')

    cp "${PATH_LATEX}/clock.tex" "${PATH_TEMP}"
    cp "${PATH_LATEX}/${FILE_INPUT}.tex" "${PATH_TEMP}"
    if [[ $LOGO != "" ]]; then
        cp -f "${LOGO}" "${PATH_TEMP}/logo-text.pdf"
    fi
    cd $PATH_TEMP

    magick -size 1x1 xc:rgba\(0,0,0,0\) "render-clock-fixed.png"

    if [[ $EXCLUDE != *"clock"* ]]; then
        # Generate clock (Creates "clock.pdf")
        pdflatex -shell-escape -synctex=0 -interaction=batchmode -file-line-error -jobname="clock-uncropped" \
        "\newcommand\FramesCurrent{$FRAMES_CURRENT}" \
        "\newcommand\FPS{$FPS}" \
        "\newcommand\Period{$PERIOD}" \
        "\newcommand\ClockHandInitialHour{$CLOCK_HAND_INITIAL_HOUR}" \
        "\newcommand\ClockHandInitialMinute{$CLOCK_HAND_INITIAL_MINUTE}" \
        "\newcommand\ClockHandInitialSecond{$CLOCK_HAND_INITIAL_SECOND}" \
        "\newcommand\ClockHandRevolutionsHour{$CLOCK_HAND_REVOLUTIONS_HOUR}" \
        "\newcommand\ClockHandRevolutionsMinute{$CLOCK_HAND_REVOLUTIONS_MINUTE}" \
        "\newcommand\ClockHandRevolutionsSecond{$CLOCK_HAND_REVOLUTIONS_SECOND}" \
        "\newcommand\ClockEdgeWidth{$CLOCK_EDGE_WIDTH}" \
        "\input{clock.tex}"
        pdfcrop --hires --resolution 4000x4000 "clock-uncropped.pdf" "clock-cropped.pdf"

        # Rasterise and warp clock (creates "clock-distorted.png")
        magick -density 4000 "clock-cropped.pdf" -quality 100% -resize 4000x4000 "clock.png"
        if [[ $CLOCK_DISTORT == "static" ]]; then
            magick "clock.png" -alpha set -virtual-pixel transparent -interpolate Spline -distort BilinearReverse "0,0,0,0 4000,0,4000,0 0,4000,800,4000 4000,4000,3200,4000" "clock-distorted.png"
            magick "clock-distorted.png" -alpha set -virtual-pixel transparent -distort Perspective "0,0,0,0 4000,0,4000,0 0,4000,1200,4000 4000,4000,2800,4000" "clock-distorted.png"
            # Alternative stretch
            # magick "clock-distorted.png" -resize "$(identify -format "%[width]" "clock-distorted.png")x$(echo "1.2*$(identify -format "%[height]" "clock-distorted.png")" | bc -l)"\! "clock-distorted.png"
        elif [[ $CLOCK_DISTORT == "swimming" ]]; then
            magick "clock.png" -alpha set -virtual-pixel transparent -interpolate Spline -distort BilinearReverse "0,0,$(echo "800 * s(4*a(1)*$FRAMES_CURRENT/$FRAMES_TOTAL)^2" | bc -l),0 4000,0,$(echo "4000 - 800 * s(4*a(1)*$FRAMES_CURRENT/$FRAMES_TOTAL)^2" | bc -l),0 0,4000,$(echo "800 * c(4*a(1)*$FRAMES_CURRENT/$FRAMES_TOTAL + a(1))^2" | bc -l),4000 4000,4000,$(echo "4000 - 800 * c(4*a(1)*$FRAMES_CURRENT/$FRAMES_TOTAL + a(1))^2" | bc -l),4000" "clock-distorted.png"
        elif [[ $CLOCK_DISTORT == "floating" ]]; then
            magick "clock.png" -alpha set -virtual-pixel transparent -interpolate Spline -distort BilinearReverse "0,0,0,0 4000,0,4000,0 0,4000,500,4000 4000,4000,3500,4000" "clock-distorted.png"
            magick "clock-distorted.png" -alpha set -virtual-pixel transparent -distort Perspective "0,0,0,0 4000,0,4000,0 0,4000,800,4000 4000,4000,3200,4000" "clock-distorted.png"
            MAGNITUDE=500
            magick "clock-distorted.png" -alpha set -virtual-pixel transparent -interpolate Spline -distort BilinearReverse "0,0,$(echo "$MAGNITUDE * s(4*a(1)*$FRAMES_CURRENT/$FRAMES_TOTAL)^2" | bc -l),0 4000,0,$(echo "4000 - $MAGNITUDE * s(4*a(1)*$FRAMES_CURRENT/$FRAMES_TOTAL)^2" | bc -l),0 0,4000,$(echo "$MAGNITUDE * c(4*a(1)*$FRAMES_CURRENT/$FRAMES_TOTAL + 0*a(1))^2" | bc -l),4000 4000,4000,$(echo "4000 - $MAGNITUDE * c(4*a(1)*$FRAMES_CURRENT/$FRAMES_TOTAL + 0*a(1))^2" | bc -l),4000" "clock-distorted.png"
        else
            mv -f "clock.png" "clock-distorted.png"
        fi

        if [[ $CLOCK_BLUR == true ]]; then
            # Add motion-blur effect
            magick -size $(identify -format "%[width]x%[height]" "clock-distorted.png") -define gradient:direction=North gradient:black-white "mask.png"
            # magick "clock-distorted.png" -write-mask mask.png -virtual-pixel tile -blur 0x0 -motion-blur 0x80+90 +write-mask "clock-distorted.png"
            magick "clock-distorted.png" -write-mask mask.png -virtual-pixel tile -blur 0x0 -motion-blur 0x$(echo "80 * s(4*a(1)*$FRAMES_CURRENT/$FRAMES_TOTAL)^2" | bc -l)+90 +write-mask "clock-distorted.png"
        fi

        if [[ $EXCLUDE != *"wormhole"* ]]; then
            # Create wormhole and composite clock (Creates "render-first.pdf")
            pdflatex -shell-escape -synctex=0 -interaction=batchmode -file-line-error -jobname="render-first" \
            "\newcommand\FramesCurrent{$FRAMES_CURRENT}" \
            "\newcommand\FPS{$FPS} \newcommand\Period{$PERIOD}" \
            "\newcommand\WormholeCircles{$WORMHOLE_CIRCLES}" \
            "\newcommand\WormholeSectors{$WORMHOLE_SECTORS}" \
            "\newcommand\WormholeRotations{$WORMHOLE_ROTATIONS}" \
            "\newcommand\ClockPositionCyclesHorizontal{$CLOCK_POSITION_CYCLES_HORIZONTAL}" \
            "\newcommand\ClockPositionCyclesVertical{$CLOCK_POSITION_CYCLES_VERTICAL}" \
            "\newcommand\ClockPositionAmplitudeHorizontal{$CLOCK_POSITION_AMPLITUDE_HORIZONTAL}" \
            "\newcommand\ClockPositionAmplitudeVertical{$CLOCK_POSITION_AMPLITUDE_VERTICAL}" \
            "\input{$FILE_INPUT.tex}"

            # Fix transparency
            # This extracts the rasterised "clock-distorted.png" from "render-first.pdf" with a mask [creating "render-clock-fixed.png"],
            # and renames "clock-distorted.png" to "clock-warped.png" so that the masked clock can be composited into the logo via a second pass of $FILE_INPUT.tex
            pdfimages -png "render-first.pdf" "render-clock-masks"
            composite -compose CopyOpacity "render-clock-masks-001.png" "render-clock-masks-000.png" "render-clock-fixed.png"
        else
            magick "clock-distorted.png" -quality 100% -density 4000 "render-second.pdf"
        fi

        mv -f "clock-distorted.png" "clock-warped.png" # Move it out of the way for the second pass of pdflatex
    fi

    if [[ $EXCLUDE != *"wormhole"* ]]; then
        pdflatex -shell-escape -synctex=0 -interaction=batchmode -file-line-error -jobname="render-second" \
        "\newcommand\FramesCurrent{$FRAMES_CURRENT}" \
        "\newcommand\FPS{$FPS}" \
        "\newcommand\Period{$PERIOD}" \
        "\newcommand\WormholeCircles{$WORMHOLE_CIRCLES}" \
        "\newcommand\WormholeSectors{$WORMHOLE_SECTORS}" \
        "\newcommand\WormholeRotations{$WORMHOLE_ROTATIONS}" \
        "\newcommand\ClockPositionCyclesHorizontal{$CLOCK_POSITION_CYCLES_HORIZONTAL}" \
        "\newcommand\ClockPositionCyclesVertical{$CLOCK_POSITION_CYCLES_VERTICAL}" \
        "\newcommand\ClockPositionAmplitudeHorizontal{$CLOCK_POSITION_AMPLITUDE_HORIZONTAL}" \
        "\newcommand\ClockPositionAmplitudeVertical{$CLOCK_POSITION_AMPLITUDE_VERTICAL}" \
        "\input{$FILE_INPUT.tex}"
    fi

    # Copy over the PDF if required (for the cover outputs)
    if [[ $FORMAT == *"pdf"* ]]; then
        mv -f "${PATH_TEMP}/render-second.pdf" "${PATH_OUTPUT}/${FILE_OUTPUT}.pdf"
    else
        if [[ $TRANSPARENCY == false ]]; then
            magick -density 800 "render-second.pdf" -background white -alpha remove -alpha off -flatten -sharpen 0x1.0 -gaussian-blur 0.00 -quality 100% "${FILE_OUTPUT}.png"
        else
            magick -density 800 "render-second.pdf" -background transparent -flatten -sharpen 0x1.0 -gaussian-blur 0.00 -quality 100% "${FILE_OUTPUT}.png" # Also, -background white -transparent white (and variations thereof)
        fi
        magick "${FILE_OUTPUT}.png" -gravity $GRAVITY -crop $ASPECT_RATIO -resize $RESOLUTION_HORIZONTAL "${FILE_OUTPUT}.webp"

        PADDING=$(printf '0%.0s' $(seq 1 ${#FRAMES_TOTAL}))
        PADDED="${PADDING}$((FRAMES_CURRENT + ONE))"
        FILENAME="${FILE_OUTPUT}-frame-${PADDED: -${#FRAMES_TOTAL}}"
        echo $FILENAME
        echo "${PATH_TEMP}/${FILE_OUTPUT}.webp"
        echo "${PATH_OUTPUT}/${FILENAME}.webp"

        mv -f "${PATH_TEMP}/${FILE_OUTPUT}.webp" "${PATH_OUTPUT}/${FILENAME}.webp"

        # Make the static image using the first frame
        if [[ $FRAMES_CURRENT == 0 ]]; then
            cp -f "${PATH_OUTPUT}/${FILENAME}.webp" "${PATH_OUTPUT}/${FILE_OUTPUT}.webp"
            magick "${PATH_OUTPUT}/${FILE_OUTPUT}.webp" "${PATH_OUTPUT}/${FILE_OUTPUT}.png"
        fi
    fi

    cd $PATH_OUTPUT
    rm -rf $PATH_TEMP || echo "Already done."
    ) &

    background=( $(jobs -p) )
    if (( ${#background[@]} == $THREADS )); then
        wait -n
    fi

done
wait
)

if [[ $FORMAT == *"pdf"* ]]; then
    exit 1
fi

# Make the animation from the frames
cd $PATH_OUTPUT
FRAMES=( )
SECOND=1000 # Milliseconds
FRAMETIME=$(echo "$SECOND/$FPS" | bc -l)
FRAMETIME=$(printf '%.0f' $FRAMETIME)
for f in ${FILE_OUTPUT}-frame-*.webp ; do
    FRAMES+=( -frame "$f" +${FRAMETIME}+0+0+0-b )
done
webpmux "${FRAMES[@]}" -loop 0 -bgcolor 0,0,0,0 -o "${FILE_OUTPUT}-animated-uncompressed.webp"
magick "${FILE_OUTPUT}-animated-uncompressed.webp" -resize $RESIZE -quality $QUALITY% "${FILE_OUTPUT}-animated-${QUALITY}compressed.webp"
# Can alternatively compress each frame like so:
# for f in ${FILE_OUTPUT}-frame-*.webp ; do
#     magick $f $f.webp
#     cwebp $f.webp -resize $RESIZE 0 -m 6 -q $QUALITY -o "$f-compressed.webp"
# done
# But the muxed animated WebP is larger by 10% ~ 30% than its imagemagick-compressed counterpart (comparing roughly equivalent quality)
# So the latter seems to be (surprisingly?) a better choice for compression...

# Remove all rendered frames, leaving just the animation(s)
if [[ $CLEAN == true ]]; then
    for f in ${FILE_OUTPUT}-frame-*.webp ; do
        rm -f "$f"
    done
fi

echo $PATH_LATEX
