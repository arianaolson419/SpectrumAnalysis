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

print 'testing...'
song_file = '/home/arianaolson/SpectrumAnalysis/02_White_Freckles.wav' 		# song_file must be a .wav file
song_name = str(os.path.splitext(song_file.split('/')[-1])[0])


if __name__ == '__main__':

	""" Open the file and get attributes """
	song = wave.open(song_file, 'r')			# open wave file as read only
	frames = song.getnframes()					# number of individual data snippets (frames) in song
	frame_rate = song.getframerate()			# frequency of frames per second
	print "Frames: %s" % frames
	sample_width = song.getsampwidth()			# given discretized signal, get the width of each portion (sample)
	song_length = frames / float(frame_rate)	# determine the length of the song by dividing frames by frequency
	channels = song.getnchannels()
	print "Channels: %s"
	song_data = song.readframes(frames)			# reads & returns each frame of audio as a string of bytes

	song.close()								# close song file, we don't need it anymore


	""" Unpack the binary data from 
		song_data into an array """
	song_data = struct.unpack('{}h'.format(frames*2), song_data)

	
	""" Initialize FFT variables """
	fourier_rate = 24							# frames per second
	fourier_width = 1.0/fourier_rate			# width of each discrete fourier
	fourier_index = \
		fourier_width * float(frame_rate)		# index is width times frame frequency

	total_transforms = \
		int(round(song_length*fourier_rate))	# determines total number of fourier transforms by multiplying the song length by the fourier rate
	fourier_spacing = \
		round(fourier_width*float(frame_rate))	# determines which points at which discretize fourier transform

	last_pt = \
		int(round(song_length*float(frame_rate) + fourier_index))

	freq = frame_rate / fourier_index * np.arange(fourier_index)

	band_width = 1.0 / fourier_width			# determine band width


	""" Convert Frequency (input) to Index (output) """
	def FreqToIndex(f):
		# if f (frequency) is lower than bandwidth of spectrum[0], return 0
		if f < band_width/2:
			return 0
		# if f is larger than 1/2 the frame rate minus 1/2 the band width, return fourier index - 1
		if f > (frame_rate/2) - band_width/2:
			return fourier_index - 1
		fraction = float(f) / float(frame_rate)	
		index = round(fourier_index * fraction)	# converted frequency to index
		return index

	fft_averages = [] 							# initialize an array for fft averages
	all_fft_avgs = [] 							# initialize an array to contain all ffts over all frames

	""" Average the frequencies in each band """
	def AvgFftBands(fft_array):
		num_bands = 12							# num_bands based on frequency bands (12 notes in 1 octave)
		del fft_averages[:]						# reinitialize an empty fft_averages list
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

	
	# for offset in range(0, total_transforms):
	# 	start = int(offset * fourier_index)
	# 	end = int((offset * fourier_index) + fourier_index -1)

	# 	print "Processing sample %i of %i (%d seconds)" % (offset + 1, total_transforms, end/float(frame_rate))
	# 	sample_range = song_data[start:end]

		# """ This is where we actually use FFT """
		# fft_data = abs(np.fft.fft(sample_range))

		# fft_data *= ((2**.5)/fourier_index)	# normalize it a second time to make numbers sensible
		# AvgFftBands(fft_data)
		# bar_levels = fft_averages
		# bar_levels = np.transpose(bar_levels)
		# all_fft_avgs.append(bar_levels)

		# """ Uncomment this if you want to make bar graphs """
		# x_axis = range(0,12)
		# y_axis = fft_averages
		# width = 0.35
		# p1 = plt.bar(x_axis, y_axis, width, color='r')
		# print next

		# filename = str('frame_%05d' % offset) + '.png'
		# plt.savefig(filename, dpi=100)
		# plt.close()


	""" Uncomment this if you want to save FFT Data to a CSV """
	# filename = str(song_name) + 'Data' + '.csv'
	# np.savetxt(filename, all_fft_avgs, delimiter=",")

	print "Done!"