'''
MUSIC VISULAIZER WEB APP

a simple web app that allows the user to choose a song from a list 
to initialize the LED visualizer and play the song when the 
"Start!" button is pressed

team: SpectrumAnalysis1 (Ariana Olson, Harper Owen, Paige Pfenninger)
author: Ariana Olson

'''
from flask import *
import os, sys
import playsong
# import AV_LED
app = Flask(__name__)

#keys correspond to the choices in the dropdown menu.
#first value is the title, second the file location, third the FFT data.
songs = {'song1': ['White Freckles','audio/White_Freckles.wav', '../White_FrecklesData.csv'],	
	'song2': ['Gooey', 'audio/Gooey.wav', '../GooeyData.csv'],
	'song3': ['Sine Wave', 'audio/440_sine.wav', '../440_sineData.csv'],
	'song4': ['Disciples', 'audio/Disciples.wav', '../DisciplesData.csv']}

@app.route('/')
def selection_page():
	'''Displays the initial page with the big red button (index.html)'''
	return render_template('index.html') #displays the button page
@app.route('/play_song', methods=['GET', 'POST'])
def test(song=None):
	'''displays the page letting the user know what song is being played (play_song.html). 
	Also runs a python script with arguments on the computer'''
	song = request.form['song'] #determines which song was selected
	playsong.playit(songs[song][1]) #plays the song
	# AV_LED.ShowLEDs(songs[song[2]])
	return render_template('play_song.html', song=songs[song][0]) #displays the play_song page

if __name__ == '__main__':
	app.run(debug=True)
