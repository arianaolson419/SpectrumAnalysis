from flask import *
import sys
app = Flask(__name__)

@app.route('/')
def selection_page():
	'''Displays the initial page with the big red button (index.html)'''
	return render_template('index.html') #displays the button page
@app.route('/play_song', methods=['GET', 'POST'])
def test(song=None):
	'''displays the page letting the user know what song is being played and visualized (play_song.html). 
	Also runs a python script with arguments on the computer'''
	song = request.form['song'] 
	sys.argv = ['test.py', 'Ariana', 1, 'O']
	execfile(sys.argv[0])
	# sys.argv = ['AV_FFT.py', '/home/arianaolson/SpectrumAnalysis/02_White_Freckles.wav'] #set system arguments
	# execfile('AV_FFT.py') #executes the script. file name must == sys.argv[0]
	return render_template('play_song.html', song=song) #displays the play_song page

if __name__ == '__main__':
	app.run()
