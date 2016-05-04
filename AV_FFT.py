"""
	We referenced an example of an audio visualizer from Xander Shephard. 
	Github repo is here: https://github.com/n00bsys0p/python-visualiser 
	For the most part we are utilizing his structure, but we've
	commented every line to show that we understand what is happening
	and we've added some parts to fit our model which are specified below
"""

import sys
import os
import wave
import struct
import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
from matplotlib import pylab
import matplotlib.pyplot as plt
import subprocess as sp

# song_file must be a .wav file
song_file = 'Web App/audio/440_sine.wav'
song_name = str(os.path.splitext(song_file.split('/')[-1])[0])


""" Open the file and get attributes """
# open wave file as read only
song = wave.open(song_file, 'r')
# number of individual data snippets (frames) in song
frames = song.getnframes()
# frequency of frames per second
frame_rate = song.getframerate()
# given discretized signal, get the width of each portion (sample)
sample_width = song.getsampwidth()
# determine the length of the song by dividing frames by frequency
song_length = frames / float(frame_rate)
channels = song.getnchannels()
# reads & returns each frame of audio as a string of bytes
song_data = song.readframes(frames)

song.close()

""" Unpack the binary data from 
	song_data into an array """
song_data = struct.unpack('{}h'.format(frames*2), song_data)


""" Initialize FFT variables """
# frames per second
fourier_rate = 24
# width of each discrete fourier
fourier_width = 1.0/fourier_rate
# index is width times frame frequency
fourier_index = fourier_width * float(frame_rate)

# determines total number of fourier transforms by multiplying the song length by the fourier rate
total_transforms = int(round(song_length*fourier_rate))
# determines which points at which discretize fourier transform
fourier_spacing = round(fourier_width*float(frame_rate))

last_pt = int(round(song_length*float(frame_rate) + fourier_index))

freq = frame_rate / fourier_index * np.arange(fourier_index)

# determine band width
band_width = 1.0 / fourier_width

# initialize an array for fft averages
fft_averages = []
# initialize an array to contain all ffts over all frames
all_fft_avgs = []


""" Convert Frequency (input) to Index (output) """
def FreqToIndex(f):
	# if f (frequency) is lower than bandwidth of spectrum[0], return 0
	if f < band_width/2:
		return 0
	# if f is larger than 1/2 the frame rate minus 1/2 the band width, return fourier index - 1
	if f > (frame_rate/2) - band_width/2:
		return fourier_index - 1
	fraction = float(f) / float(frame_rate)
	# converted frequency to index
	index = round(fourier_index * fraction)
	return index



""" Average the frequencies in each band """
def AvgFftBands(fft_array):
	# num_bands based on frequency bands (12 notes in 1 octave)
	num_bands = 15
	# reinitialize an empty fft_averages list
	del fft_averages[:]
	for band in range(0, num_bands):
		avg = 0.0

		if band == 0:
			lowFreq = int(0)
		else:
			lowFreq = int(int(frame_rate / 2) / float(2 ** (num_bands - band)))
		hiFreq = int((frame_rate / 2) / float(2 ** ((num_bands-1) - band)))
		lowBound = int(FreqToIndex(lowFreq))
		hiBound = int(FreqToIndex(hiFreq))
		for j in range(lowBound, hiBound):
			avg += fft_array[j]

		avg /= (hiBound - lowBound + 1)
		fft_averages.append(avg)

def RemapFftInterval(fft_array):
	bar_vals = []
	mean = np.mean(fft_array)
	stnd = np.std(fft_array)
	output_max = mean + stnd*3
	leds = 5
	for i in range(len(fft_array)-1):
		ratio = output_max / leds
		new_val = np.ceil((fft_array[i] / ratio))
		if new_val >= leds:
			new_val = leds
			bar_vals.append(new_val)
		elif 1 <= new_val < leds: 
			bar_vals.append(new_val)
		else:
			bar_vals.append(0)
	return bar_vals

for offset in range(0, total_transforms):
	start = int(offset * fourier_index)
	end = int((offset * fourier_index) + fourier_index -1)

	sample_range = song_data[start:end]

	""" This is where we actually use FFT """
	fft_data = abs(np.fft.fft(sample_range))

	fft_data *= ((2**.5)/fourier_index)	# normalize it a second time to make numbers sensible
	AvgFftBands(fft_data)
	bar_levels = RemapFftInterval(fft_averages)
	bar_levels = np.transpose(bar_levels)
	all_fft_avgs.append(bar_levels)

	""" Uncomment this if you want to make bar graphs """
	# x_axis = range(0,12)
	# y_axis = fft_averages
	# width = 0.35
	# p1 = plt.bar(x_axis, y_axis, width, color='r')
	# print next

	# filename = str('frame_%05d' % offset) + '.png'
	# plt.savefig(filename, dpi=100)
	# plt.close()

	# command1 = ['/usr/bin/ffmpeg' '-f' 'image2' '-r' '24' '-i' 'frame_%05d.png' '-vcodec mpeg4' '-y' 'movie.mp4']
	# pipe = sp.Popen(command1, stdin=sp.PIPE,stdout=sp.PIPE, stderr=sp.PIPE)

""" Uncomment this if you want to save FFT Data to a CSV """
filename = str(song_name) + 'Data' + '.csv'
np.savetxt(filename, all_fft_avgs, delimiter=",")

print "Done!"