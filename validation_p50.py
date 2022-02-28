import numpy as np
import matplotlib.pyplot as plt
from functions import load_rawsignal,extract_signal_freq,check_pulses_freq
from tqdm import tqdm

signal,t,fs=load_rawsignal(r'C:\Users\ezxiaav\Documents\motion_artifacts\P50\PPG.txt',100)
len_signal=len(signal)
n=len_signal/250
segments=np.array_split(signal, n)
i=0
for i in tqdm(range(230,240)):
    i+=1
    f=extract_signal_freq(segments[i])
    #print('fundamental frequency =',f)
    f=np.array(f)
    if len(f)>1:
        label=0
    elif  f>= 0.0133 and f<= 0.03:
        f_std=check_pulses_freq(segments[i])
        print(f_std > float(0))
        if f_std > float(0.008):
            label=0
        elif f_std<=float(0.008):
            label=1
    else:
        label=0

    print("label=", label)
    plt.figure()
    plt.plot(segments[i])
    plt.title('# '+str(i)+' PPG segment')
    plt.xlabel('# samples') 
    plt.ylabel('Amplitude')
    plt.show()