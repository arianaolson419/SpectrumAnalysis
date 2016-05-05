'''Defining the functions called by the web app (page.py)no'''
import subprocess
import time 

def playit(song):
	'''Plays a given song'''
	cmd = 'aplay ' + song
	popen = subprocess.Popen(cmd, shell=True)
	time.sleep(2)
	popen.communicate()


if __name__== '__main__':
	song = "audio/White_Freckles.wav"
	playit(song)

