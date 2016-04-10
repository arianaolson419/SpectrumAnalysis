#!/bin/bash

if [ $# -lt 1 ]; then
  echo "You must supply a mono-mixed wave file as the first argument."
  exit 1
fi

[[ -w frame_*.png ]] && rm frame_*.png

./plotvals.py $1

ffmpeg -f image2 -r 24 -i frame_%05d.png -vcodec mpeg4 -y movie.mp4 					# change movie.mp4 to yourtitle.mp4
ffmpeg -i input.wav -c:a libfdk_aac -vbr 3 output.m4a									# change input.wav to yourfile.wav and output.m4a to yourtitle.m4a
ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental output.mp4 	# change all the imputs and outputs