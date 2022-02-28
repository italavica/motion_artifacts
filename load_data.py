
import pandas as pd
import matplotlib.pyplot as plt
from functions import discard_empty_records, histogram
from tqdm import tqdm
import numpy as np


# with open(r'C:\Users\ezxiaav\Desktop\SureSat-Simon\PPG_records.txt') as f:
#     records_list = f.readlines()
# f.close()

# print(type(records_list[0]))
# print(len(records_list))

# updated_list = open('PPG_records_updated.txt', 'w')
# record_list_updated= discard_empty_records(records_list,updated_list)
# updated_list.close()

# print(len(record_list_updated))

with open(r'C:\Users\ezxiaav\Documents\motion_artifacts\PPG_records_updated.txt') as f:
    records_list_updated = f.readlines()
f.close()
len_signals=[]

for path in tqdm(records_list_updated):
    path= str.rstrip(path)
    df = pd.read_csv (path)
    len_signal=len(df.loc[:,'Green[raw]'])
    len_signals.append(len_signal)
    # plt.figure()
    # plt.plot(df.loc[:,'Green[raw]'])
    # plt.title('# '+ path[-39:]+' PPG signal')
    # plt.xlabel('# samples') 
    # plt.ylabel('Amplitude')
    # plt.show()

print(type(len_signals))
print(len_signals)
len_signals = np.array(len_signals)
print(len(len_signals))

# plt.figure()
# plt.plot(len_signals)
# plt.title('length of green signals (# of samples)')
# plt.xlabel('# samples') 
# plt.ylabel('length')
# plt.show()

name='length of green signals (# of samples)'
len_signals_series=pd.Series(len_signals)
histogram(len_signals_series,name,20)

# len_file = open("lengths_signals.txt", "w")
# for element in len_signals:
#     np.savetxt(len_file, element)
# len_file.close()
#len_signals = np.loadtxt("lengths_signals.txt")
#print(len_signals)




