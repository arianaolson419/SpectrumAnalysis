import time
import numpy as np
from neopixel import *

""" Program to Control LEDs """

# LED strip configuration:
LED_COUNT      = 150     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


""" Import FFT File """
song_dir = "GooeyData.csv"
bar_array = np.genfromtxt(song_dir, delimiter=',', dtype=None, names=True)


""" Run LEDs """
def AudioVisualizer(strip, color, led_array, LED_COUNT):
	fps = 24
	q = LED_COUNT * 2 / 12
	for frame in range(len(led_array)-1):
		for i in frame:
			if i == 0:
				for j in range(i[0]-1):
					strip.setPixelColor(j+1, color)
					strip.show()
			elif i == 1:
				for j in range(i[1]-1):
					strip.setPixelColor(2*q-j, color)
					strip.show()
			elif i == 2:
				for j in range(i[2]-1):
					strip.setPixelColor(2*q+1+j, color)
					strip.show()
			elif i == 3:
				for j in range(i[3]-1):
					strip.setPixelColor(4*q-j, color)
					strip.show()
			elif i == 4:
				for j in range(i[4]-1):
					strip.setPixelColor(4*q+1+j, color)
					strip.show
			elif i == 5:
				for j in range(i[5]-1):
					strip.setPixelColor(6*q-j, color)
					strip.show()
			elif i == 6:
				for j in range(i[6]-1):
					strip.setPixelColor(6*q+1+j, color)
					strip.show()
			elif i == 7:
				for j in range(i[7]-1):
					strip.setPixelColor(8*q-j, color)
					strip.show()
			elif i == 8:
				for j in range(i[8]-1):
					strip.setPixelColor(8*q+1+j, color)
					strip.show()
			elif i == 9:
				for j in range(i[9]-1):
					strip.setPixelColor(10*q-j, color)
					strip.show()
			elif i == 10:
				for j in range(i[10]-1):
					strip.setPixelColor(10*q+1+j, color)
					strip.show()
			elif i == 11:
				for j in range(i[11]-1):
					strip.setPixelColor(12*q-j, color)
					strip.show
		time.sleep(1/fps)


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		# Begin Animations
		AudioVisualizer(strip, Color(127, 0, 0), bar_array, LED_COUNT)

