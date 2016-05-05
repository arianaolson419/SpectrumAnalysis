#Music Visualizer

Authors: Ariana Olson, Harper Owen, Paige Pfenninger

## Description

This program creates and LED music visualizer using Fast Fourier Transforms. An LED array controlled by a Raspberry Pi lights up in time to music, displaying the FFT bars.


## How To Use It
The music visualizer comes with a few preloaded songs. To use these songs, follow the instructions below:

1. Connect the hardware components to the Raspberry Pi (see instructions under Hardware Required)
2. Run web app (page.py) in a local server from the Raspberry Pi
3. Choose a song from the list
4. Press start. The bar graph visualizer will play on the screen while the LEDs start to light up in time with the music.

### Hardware Required
Raspberry Pi and connecting cables
WS2812 LEDs
Power supply and power jack
Level shifter
Breadboard and appropriate jumper wires
[Connecting LEDs](http://popoklopsi.github.io/RaspberryPi-LedStrip/#!/ws2812)

### Creating visualization for a new song
1. In the file AV_FFT.py, change the song_file to the directory of your song of choice
2. Uncomment the Bar Graph creator section of the file and the CSV creator code(at the bottom of the page) 
3. Run the file to compile the frames of the song you created into an animation and export the csv file to your LED program
4. Add the new song to the directory in page.py and index.html.This adds the new song to the web app
5. You can now use this like all of the preloaded songs!


## Dependencies
[Flask](http://flask.pocoo.org/)

[Ffmpeg](https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu)

[Rpiws281x](https://github.com/richardghirst/rpi_ws281x)

[NumPy](http://www.numpy.org/)

[Matplotlib](http://matplotlib.org/users/installing.html)

