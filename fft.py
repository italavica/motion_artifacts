# import required modules
import numpy as np

# assign data
x = np.array([1, 2, 1, 0, 1, 2, 1, 0])

# compute DFT with optimized FFT
w = np.fft.fft(x)

# compute frequency associated
# with coefficients
freqs = np.fft.fftfreq(len(x))
print(freqs)
# extract frequencies associated with FFT values
for coef, freq in zip(w, freqs):
    if coef:
        print(freq)
		#print('{c:>6} * exp(2 pi i t * {f})'.format(c=coef,
													#f=freq))
