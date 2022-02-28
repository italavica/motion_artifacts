import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm
from scipy import stats

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

def remove_DC(signal,fs):
  def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

  DC=smooth(signal, 80)
  AC= DC - signal
  L = len(AC)        
  t= np.arange(0, L/fs, 1/fs)
  return AC,t
  

def plot(signal,signal_time,signal_name):
    L= len(signal)
    plt.figure()
    plt.plot(signal_time,signal, label=signal_name)
    plt.title(signal_name)
    plt.xlabel('Time (s)') 
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

def discard_empty_records(records_list,updated_list):
  record_list_updated=[]
  for path in tqdm(records_list):
    path= str.rstrip(path)
    df = pd.read_csv (path)
    if len(df.loc[:,'Green[raw]'])>250:
      with open('PPG_records_updated.txt', 'a') as updated_list:
        updated_list.write(path + "\n")
      record_list_updated.append(path)
  return record_list_updated


def histogram(variable_to_count,name,nbins):
  variable_to_count.plot.hist(grid=True, bins=nbins, rwidth=0.9,
                   color='#607c8e')
  plt.title('frequency of '+name)
  plt.xlabel(name)
  plt.ylabel('Counts')
  plt.grid(axis='y', alpha=0.75)
  plt.show()

def extract_signal_freq(x):
  f=[]
  # compute DFT with optimized FFT
  w = np.fft.fft(x)
  # compute frequency associated
  # with coefficients
  freqs = np.fft.fftfreq(len(x))
  # extract frequencies associated with FFT values
  firstNegInd = np.argmax(freqs < 0)
  freqs = freqs[0:firstNegInd]
  w = 2 * w[0:firstNegInd]  # *2 because of magnitude of analytic signal
  for coef, freq in zip(w, freqs):
      if abs(coef)==max(abs(w)):
        f.append(freq)
  return f

def check_pulses_freq(segment):
  L=len(segment)
  n=L/41.6
  pulses=np.array_split(segment, n)
  freqs=[]
  for pulse in pulses:
    f=extract_signal_freq(pulse)
    # if len(f)!=1:
    f=np.average(f)
    freqs.append(f)
  print(freqs)
  f_std=np.std(freqs)
  f_std=abs(f_std)
  return f_std
   
#def perfusion_index(segment):



