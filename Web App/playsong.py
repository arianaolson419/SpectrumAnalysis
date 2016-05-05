'''Defining the functions called by the web app (page.py)no'''
import subprocess

def playit(song):
	'''Plays a given song'''
	cmd = 'mplayer ' + song
	popen = subprocess.Popen(cmd, shell=True)
	popen.communicate()


if __name__== '__main__':
	song = "audio/White_Freckles.wav"
	playit(song)

