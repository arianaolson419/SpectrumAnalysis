'''Defining the functions called by the web app (page.py)no'''
import subprocess


def playit(song):
	'''Plays a given song'''
	subprocess.Popen('aplay ' + song, shell=True)

if __name__== '__main__':
	song = "/home/arianaolson/SpectrumAnalysis/02_White_Freckles.wav"
	playit(song)

