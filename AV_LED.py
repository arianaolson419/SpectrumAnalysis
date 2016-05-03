import time
import numpy as np
from neopixel import *
from math import floor

""" Program to Control LEDs """

# LED strip configuration:
LED_COUNT      = 150     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 50    # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
song_dir = "GooeyData.csv"
# Color of the lEDs goes Green, Blue, Red 
red = Color(0, 0, 255)
orange = Color(0, 127, 255)
yellow = Color(0, 255, 255)
green = Color(0, 255, 0)
blue = Color(255, 0, 0)
indigo = Color(130, 0, 75)
violet = Color(143, 0, 255)

roygbiv = [red, orange, \
	yellow, green, blue, indigo, violet]*2


""" Run LEDs """
def AudioVisualizer(song_dir, strip, LED_COUNT):
	bar_array = np.genfromtxt(song_dir, delimiter=',', dtype=None, names=True)
	fps = 24
	q = int(floor(LED_COUNT  / 15))
	for i in range(LED_COUNT):
		color = Color(0, 170, 100)
		strip.setPixelColor(i, color) #background color
	strip.show()
	for k in range(len(bar_array)): #k is the number of the frame
		pix_array = np.zeros((1, 150))
		frame = bar_array[k] #bar_array[k] is the frequency values
		for i in frame:
			for j in range(int(frame[i])):
				ind1 = q*i+j
				ind2 = q*i + q -j -1
				pix_array[0][ind1] = 1
				pix_array[0][ind2] = 1
		for i in range(len(pix_array[0])):
			if pix_array[0][i] == 1:
				color = roygbiv[i/q]
				strip.setPixelColor(i, color)
			else:
				color = Color(0, 0, 0)
				strip.setPixelColor(i, color)

		strip.show()	
		time.sleep(1/(fps*10))


# # Main program logic follows:
if __name__ == '__main__':
	# AudioVisualizer(song_dir, strip, LED_COUNT)

	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		# Begin Animations
		AudioVisualizer(song_dir, strip, LED_COUNT)