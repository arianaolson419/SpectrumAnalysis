'''Defining the functions called by the web app (page.py)no'''
import subprocess
import time 

def playit(song):
	'''Plays a given song'''
	cmd = 'mplayer ' + song
	popen = subprocess.Popen(cmd)
	popen.communicate()


if __name__== '__main__':
	song = "audio/White_Freckles.wav"
	time.sleep(2)
	playit(song)

