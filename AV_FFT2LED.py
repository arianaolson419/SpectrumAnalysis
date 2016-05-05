import csv
import numpy as np
import math


# should be 25 LEDs in each string
""" Import the csv file """
song_path = '/home/harper/Documents/SoftDes/SpectrumAnalysis/Gooey_GlassAnimalsData.csv'
song_file = open(song_path, 'r')

song_data = np.genfromtxt(song_path, delimiter=',')

""" Go through each entry in the file and 
	convert to equivalent LED amount """

ratio = (np.amax(song_data))/25
num_frames = len(song_file.readlines())
song_file.close()

LEDs = []

for i in range(num_frames):
	frame = song_data[i,:]
	for j in frame:
		x = math.floor(j/ratio)
		LEDs.append(x)

LED_data = np.reshape(LEDs, (12, num_frames))

filename = str('Testy') + 'LED_Data' + '.csv'
np.savetxt(filename, LED_data , delimiter=",")

print 'Done!'