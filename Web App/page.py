from flask import *
import os, sys
import playsong
app = Flask(__name__)

#keys correspond to the choices in the dropdown
#menu. first value is the title, second is the file location
songs = {'song1': ['White Freckles','audio/White_Freckles.wav'],	
	'song2': ['Gooey', 'audio/Gooey.wav'],
	'song3': ['Sine Wave', 'audio/440_sine.wav']}

@app.route('/')
def selection_page():
	'''Displays the initial page with the big red button (index.html)'''
	return render_template('index.html') #displays the button page
@app.route('/play_song', methods=['GET', 'POST'])
def test(song=None):
	'''displays the page letting the user know what song is being played and visualized (play_song.html). 
	Also runs a python script with arguments on the computer'''
	song = request.form['song'] 
	print songs[song][1]
	playsong.playit(songs[song][1])
	return render_template('play_song.html', song=songs[song][0]) #displays the play_song page

if __name__ == '__main__':
	app.run(debug=True)
