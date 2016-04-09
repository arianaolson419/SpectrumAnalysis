from pylab import *
from scipy.io import wavfile
import csv

sampFreq, snd = wavfile.read('440_sine.wav')
s1 = snd[:,0]
print sampFreq
timeArray = arange(0, float(len(s1)), 1)
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000 #scale to milliseconds

# plt = plot(timeArray, s1[0:len(timeArray)], color='k')
# ylabel('Amplitude')
# xlabel('Time (ms)')
# show(plt)

n = len(s1)/2
p = fft(s1)
print p

nUniquePts = ceil((n + 1)/2.0)


p = p[0:nUniquePts]
print p
p = abs(p)
p = p/float(n)
p = p**2

if n % 2 > 0:
	p[1:len(p)] = p[1:len(p)] * 2
else:
	p[1:len(p) -1] = p[1:len(p) - 1] * 2

freqArray = arange(0, nUniquePts, 1.0) * (sampFreq / n);
plt2 = plot(freqArray/1000, 10*log10(p), color='k')
xlabel('Frequency (kHz)')
ylabel('Power (dB)')
show(plt2)