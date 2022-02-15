import numpy as np
import matplotlib.pyplot as plt


def load_rawsignal(address,sampling_rate):
#def load_rawsignal(address,sampling_rate):
  # load raw ECG signal
  signal = np.loadtxt(address)


  def smooth(y, box_pts):
      box = np.ones(box_pts)/box_pts
      y_smooth = np.convolve(y, box, mode='same')
      return y_smooth

  DC=smooth(signal, 80)
  AC= DC - signal;
  fs=sampling_rate
  L = len(AC)        
  t= np.arange(0, L/fs, 1/fs)

  # AC= AC[a:b]
  # L = len(AC)     
  # t= np.arange(int(a/fs), int(a/fs)+L/fs, 1/fs)
  #t= np.arange(0, L/fs, 1/fs)
  # signal= signal[a:b]
  # L = len(signal)     
  # t= np.arange(0, L/fs, 1/fs)

  #return AC,t,fs
  return AC,t,fs

def plot(signal,signal_time,signal_name):
    L= len(signal)
    plt.figure()
    plt.plot(signal_time,signal, label=signal_name)
    plt.title(signal_name)
    plt.xlabel('Time (s)') 
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()
