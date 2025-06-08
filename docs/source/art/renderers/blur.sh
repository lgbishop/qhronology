#!/usr/bin/env bash

magick -density 200 cover-back.pdf cover-back.png
magick -size $(identify -format "%[width]x%[height]" cover-back.png) -define gradient:direction=northwest gradient:white-black mask.png

# -virtual-pixel tile -blur 0x.4 -motion-blur 0x20+45 -normalize

# magick cover-back.png -blur 0x8 -compose Blur -alpha on -compose CopyOpacity -composite mask.png -compose Over -composite out.png

# convert cover-back.png -blur 0x8 cover-back-blurred.png

# convert cover-back.png -blur 0x8 cover-back-blurred.png mask.png -compose over -composite output.jpg

magick cover-back.png -write-mask mask.png -blur 0x8 +write-mask cover-back-blurred.png
