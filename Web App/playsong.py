'''Defining the functions called by the web app (page.py)no'''
import subprocess
import pygame
import time

def playit(song):
	'''Plays a given song'''
	pygame.init()

	pygame.mixer.music.load(song)

	pygame.mixer.music.play()

	time.sleep(10)

if __name__== '__main__':
	song = "audio/White_Freckles.wav"
	playit(song)

