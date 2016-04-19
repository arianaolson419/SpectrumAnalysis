from flask import *
import os, sys
import playsong
app = Flask(__name__)

songs = {'song1': ['White_Freckles.wav']}
@app.route('/')
def selection_page():
	'''Displays the initial page with the big red button (index.html)'''
	return render_template('index.html') #displays the button page
@app.route('/play_song', methods=['GET', 'POST'])
def test(song=None):
	'''displays the page letting the user know what song is being played and visualized (play_song.html). 
	Also runs a python script with arguments on the computer'''
	song = request.form['song'] 
	playsong.playit('Gooey.wav')
	return render_template('play_song.html', song=song) #displays the play_song page

if __name__ == '__main__':
	app.run(debug=True)
