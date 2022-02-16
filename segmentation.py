import pandas as pd
import matplotlib.pyplot as plt
from functions import discard_empty_records, histogram, plot,remove_DC,extract_signal_freq
from tqdm import tqdm
import numpy as np

with open(r'C:\Users\ezxiaav\Documents\motion_artifacts\PPG_records_updated.txt') as f:
    records_list_updated = f.readlines()
f.close()


# for path in tqdm(records_list_updated):
#     path= str.rstrip(path)
#     df = pd.read_csv (path)
#     signal= df.loc[:,'Green[raw]']
#     fs=100
#     signal,signal_time= remove_DC(signal,fs)

#     plt.figure()
#     plt.plot(signal)
#     plt.title('# '+ path[-39:]+' PPG signal')
#     plt.xlabel('# samples') 
#     plt.ylabel('Amplitude')
#     plt.show()

path=records_list_updated[0]
path= str.rstrip(path)
df = pd.read_csv (path)
signal= df.loc[:,'Green[raw]']
fs=100
signal,signal_time= remove_DC(signal,fs)
L=len(signal)
n=L/250
segments=np.array_split(signal, n)
i=0
for segment in tqdm(segments):
    i+=1
    f=extract_signal_freq(segment)
    print('fundamental frequency =',f)
    plt.figure()
    plt.plot(segment)
    plt.title('# '+str(i)+' PPG segment')
    plt.xlabel('# samples') 
    plt.ylabel('Amplitude')
    plt.show()


# n=L/250
# new_signal=np.array_split(AC, n)
# print('new signal type ',type(new_signal))

# i=0
# diff=[]
# for segment in new_signal:
#     i+=1
#     d=min(segment)-max(segment)
#     diff.append(d)
#     print('max diff '+str(i)+'= ', d)
#     plt.figure()
#     plt.plot(segment)
#     plt.title('# '+str(i)+' PPG segment')
#     plt.xlabel('# samples') 
#     plt.ylabel('Amplitude')
#     plt.show()
# print('max of all segments =',max(diff))  
#     # label = int(input("label:"))
#     # labels.append(label)
#     # print("labels: ", labels))