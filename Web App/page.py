from flask import *
app = Flask(__name__)

@app.route('/')
def selection_page():
	# return "Hello"
	return render_template('index.html')
@app.route('/play_song', methods=['GET', 'POST'])
def test(song=None):
	song = request.form['song']
	print song
	return render_template('play_song.html', song=song)

if __name__ == '__main__':
	app.run()
