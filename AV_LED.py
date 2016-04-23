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


""" Import FFT File """
song_dir = "GooeyData.csv"
bar_array = np.genfromtxt(song_dir, delimiter=',', dtype=None, names=True)


""" Run LEDs """
def AudioVisualizer(strip, led_array, LED_COUNT):
	fps = 24
	q = int(floor(LED_COUNT  / 12))
	old_num_pixels = 0
	for k in range(len(led_array)):
		frame = led_array[k]
		for i in frame:
			if i == 0:
				for j in range(int(frame[0])-1):
					color = Color(127, 0, 0)
					strip.setPixelColor(j+1, color)
					# strip.show() 
			elif i == 1:
				for j in range(int(frame[1])-1):
					color = Color(0, 127, 0)
					strip.setPixelColor(2*q-j, color)
					# strip.show()
			elif i == 2:
				for j in range(int(frame[2])-1):
					color = Color(0, 0, 127)
					strip.setPixelColor(2*q+1+j, color)
					# strip.show()
			elif i == 3:
				for j in range(int(frame[3])-1):
					color = Color(127, 0, 0)
					strip.setPixelColor(4*q-j, color)
					# strip.show()
			elif i == 4:
				for j in range(int(frame[4])-1):
					color = Color(0, 127, 0)
					strip.setPixelColor(4*q+1+j, color)
					# strip.show
			elif i == 5:
				for j in range(int(frame[5])-1):
					color = Color(0, 0, 127)
					strip.setPixelColor(6*q-j, color)
					# strip.show()
			elif i == 6:
				for j in range(int(frame[6])-1):
					color = Color(127, 0, 0)
					strip.setPixelColor(6*q+1+j, color)
					# strip.show()
			elif i == 7:
				for j in range(int(frame[7])-1):
					color = Color(0, 127, 0)
					strip.setPixelColor(8*q-j, color)
					# strip.show()
			elif i == 8:
				for j in range(int(frame[8])-1):
					color = Color(0, 0, 127)
					strip.setPixelColor(8*q+1+j, color)
					# strip.show()
			elif i == 9:
				for j in range(int(frame[9])-1):
					color = Color(127, 0, 0)
					strip.setPixelColor(10*q-j, color)
					# strip.show()
			elif i == 10:
				for j in range(int(frame[10])-1):
					color = Color(0, 127, 0)
					strip.setPixelColor(10*q+1+j, color)
			strip.show()
		# 	elif i == 11:
		# 		for j in range(int(frame[11])-1):
		# 			strip.setPixelColor(12*q-j, color)
		# 			strip.show
		# time.sleep(1/fps)


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		# Begin Animations
		AudioVisualizer(strip, bar_array, LED_COUNT)
		color = blah

