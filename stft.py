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
from Orange.data import *

#create a random number or string...
rng = np.random.default_rng()

#define constants
SAMPLE_RATE = 44100 #hz
DURATION = 5 # sec

fs =10e3
N = 1e5
amp = 2 * np.sqrt(2)
noise_power = 0.01 * fs / 2
return_onesided=True

#Setup variables


time = np.arange(N) / float(fs)
mod = 500*np.cos(2*np.pi*0.25*time)
carrier = amp * np.sin(2*np.pi*3e3*time + mod)
noise = rng.normal(scale=np.sqrt(noise_power), size =time.shape)
noise *= np.exp(-time/5)

#create table domain
#color = DiscreteVareable("color" , values=["orange", "green" ] )
#data = Table(domain, [ [ "feature0", "feature1" ] ] )
#domain = Domain([0, 1 ])
#created signal #commented out noise to compare whats coming in. 
x = carrier #+ noise

#take in data table
indata=in_data

#print table data in should be same as generated data... it varies by noise... 
print(x[0])    #prints x or xy 
print(indata[0][0])    #prints x or xy 
#print(indata[0])   #prints x or xy transpose could print a column or send it if a column was selected and transposed. 

#perform STFT 
#fs sampling freq of time series  
#nperseg=1000 length of segment changes number of rows to nn samples out and window sizew for labled data real time.. 
#f, t, Zxx = signal.stft(x, fs, nperseg=1000)
#f, t, Zxx = signal.stft(indata[0], fs, nperseg=1000)
f, t, Zxx = signal.stft(indata[0], fs, nperseg=200)

#Plot output
plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=amp, shading='gouraud')


plt.title('STFT magnitude')
plt.ylabel('freq. hz')
plt.xlabel('time sec')
plt.show()


a = numpy.array(Zxx)
t = Orange.data.Table(a)

N=SAMPLE_RATE * DURATION




out_data = t
#print(Zxx.shape[0])
#print(Zxx.shape[1])
#print(np.size(Zxx, 0))
#print(np.size(Zxx, 1))
#print(Zxx)
