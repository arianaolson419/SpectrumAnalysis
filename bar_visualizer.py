import pygame 
import os, sys
import time
import csv


class bar(object):

	def __init__(self, amplitude, min_frequency, max_frequency,  screen_height, color = [50, 50, 50]):
		"""
		Creates a rectangular bar object
		"""
		self.amplitude = amplitude
		self.min_frequency = min_frequency
		self.max_frequency = max_frequency
		self.color = color
		self.rect = pygame.Rect(min_frequency, (screen_height - self.amplitude), (self.max_frequency - self.min_frequency), self.amplitude)

	def update_bar(self, old_height):
		change =  old_height - self.amplitude
		pygame.Rect.inflate_ip(self.rect, 0, change)

	def draw_bar(self, Surface):
		pygame.draw.rect(Surface, self.color, self.rect)


class bar_main():
	def __init__(self, width=800,height=600):
		"""Makes the window and displays it"""

		# initializes pygame
		pygame.init()
		pygame.display.init()

		# sets window size
		self.width = width
		self.height = height

		# creates the window
		self.window = pygame.display.set_mode((self.width, self.height))


	def main_loop(self):

		a = 300	# sets initial bar height
		
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# updates the Surface that everything is displaying on
			self.background = pygame.Surface(self.window.get_size())
			self.background = self.background.convert()
			self.background.fill((100,15,15))
			b = bar(a, 200, 300, self.height)
			b.draw_bar(self.background)
			self.window.blit(self.background, (0,0))
			# refreshes the display and makes all of the changes visisble
			pygame.display.flip()
			time.sleep(0.01) #delay between stuff
			a -= 2 #sets new bar height

if __name__ == "__main__":
	newGame = bar_main()
	newGame.main_loop()

