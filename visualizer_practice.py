from math import sqrt
import wave
import struct
wave_file = wave.open(\
	'/home/arianaolson/SpectrumAnalysis/02_White_Freckles.wav', 'r')
data_size = wave_file.getnframes()
sample_rate = wave_file.getframerate()
sample_width = wave_file.getsampwidth()
duration = data_size / float(sample_rate)

sound_data = wave_file.readframes(data_size)
wave_file.close()

unpack_fmt = '%dh' % (data_size)
sound_data = struct.unpack(unpack_fmt, sound_data)