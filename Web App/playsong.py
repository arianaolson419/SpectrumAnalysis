import pygame
import time


def playit(song):
	pygame.init()

	pygame.mixer.music.load(song)

	pygame.mixer.music.play()

	time.sleep(10)

if __name__== '__main__':
	song = "/home/arianaolson/SpectrumAnalysis/02_White_Freckles.wav"
	playit(song)