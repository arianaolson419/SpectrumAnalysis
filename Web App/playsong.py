'''Defining the functions called by the web app (page.py)no'''
import pygame
import time


def playit(song):
	'''Plays a given song
	song: file location of .wav or .mp3 audio file
	'''
	pygame.init()
	pygame.mixer.music.load(song)
	pygame.mixer.music.play()
	time.sleep(10)

if __name__== '__main__':
	song = "/home/arianaolson/SpectrumAnalysis/02_White_Freckles.wav"
	playit(song)