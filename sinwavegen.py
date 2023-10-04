#Orange Widget Python to perform STFT short term foier Transform on EEG or sensor signals

#Include nessisary Libraries

import Orange
import numpy as np
import numpy
from Orange.data import Table, Domain, ContinuousVariable, DiscreteVariable
import scipy, matplotlib
scipy.fft
from scipy.fft import fft, fftfreq
from scipy import signal
import matplotlib.pyplot as plt


rng = np.random.default_rng()

#define constants
SAMPLE_RATE = 44100 #hz
DURATION = 5 # sec

fs =10e3
N = 1e5
amp = 2 * np.sqrt(2)
noise_power = 0.01 * fs / 2

#Setup variables

time = np.arange(N) / float(fs)
mod = 500*np.cos(2*np.pi*0.25*time)
carrier = amp * np.sin(2*np.pi*3e3*time + mod)
noise = rng.normal(scale=np.sqrt(noise_power), size =time.shape)
noise *= np.exp(-time/5)

#commented out noise to find how data is passed otherwise noise made it hard to track. 
x = carrier + noise

#indata=in_data

#print(indata[0][0])#prints x or xy transpose could print a column or send it if a column was selected and transposed. 

#generated data is in the shape of a 1 d array x .... think of as row 
#send x before fft to send data. 
print(x[0])
#print(indata[0])#prints x or xy transpose could print a column or send it if a column was selected and transposed. 

#perform STFT
f, t, Zxx = signal.stft(x, fs, nperseg=1000)
#f, t, Zxx = signal.stft(indata[0], fs, nperseg=1000)

#Plot output
plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=amp, shading='gouraud')
plt.show()

#new_X = np.log(in_data.X)

#this table code for fft data
a = numpy.array(Zxx)
t = Orange.data.Table(np.abs(a))

#this table code for pre fft x data. 
b = numpy.array(x,ndmin=2)
tsin = Orange.data.Table(b)

N=SAMPLE_RATE * DURATION


#yf = fft(new_X)
#yf= np.abs(yf)
xf = fftfreq(N, 1 / SAMPLE_RATE)


out_data = tsin
#print(Zxx.shape[0])
#print(Zxx.shape[1])
#print(np.size(Zxx, 0))
#print(np.size(Zxx, 1))
#print(Zxx)
print(tsin)
