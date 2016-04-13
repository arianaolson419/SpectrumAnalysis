from flask import *
import sys
import subprocess
app = Flask(__name__)

@app.route('/')
def selection_page():
	# return "Hello"
	return render_template('index.html')
@app.route('/play_song', methods=['GET', 'POST'])
def test(song=None):
	song = request.form['song']
	sys.argv = ['AV_FFT.py', '/home/arianaolson/SpectrumAnalysis/02_White_Freckles.wav']
	execfile('AV_FFT.py')
	# subprocess.call([sys.executable, 'test.py', '1'])
	# subprocess.call([sys.executable, 'AV_FFT.py', '/home/arianaolson/SpectrumAnalysis/02_White_Freckles.wav'])
	return render_template('play_song.html', song=song)

if __name__ == '__main__':
	app.run()
