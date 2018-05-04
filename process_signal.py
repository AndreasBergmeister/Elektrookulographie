from scipy.interpolate import interp1d
from scipy.signal import butter, lfilter
import numpy as np
from matplotlib import pyplot as plt

def interpolate(x, y, frequency):
    # Calculate periodical x array with specific length
    length = x[-1]
    samples_amount = int(length * frequency)
    period_length = 1 / frequency
    # Create list with x-values for the given frequency
    # First value has to be greater or equal the first value of the input
    x_new = [period_length * i for i in range(samples_amount) if period_length * i >= x[0]]
    
    # Calculate interpolated y values
    y_new = [interp1d(x, y)(i).tolist() for i in x_new]

    return x_new, y_new

def fft(x, y):
    # Get real amplitudes of FFT (only in postive frequencies)
    fft_values = np.absolute(np.fft.rfft(y))

    # Get frequencies for amplitudes in Hz
    dt = x[1] - x[0]
    fft_freq = np.fft.rfftfreq(len(y), dt)

    return fft_freq, fft_values

    # # Plot
    # plt.plot(fft_freq, fft_values)
    # plt.show()

def butter_bandpass_filter(data, lowcut, highcut, fs, order=1):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq

    b, a = butter(order, [low, high], btype='band')
    y = lfilter(b, a, data)
    return y

def butter_highpass_filter(data, highcut, fs, order=1):
    nyq = 0.5 * fs
    high = highcut / nyq

    b, a = butter(order, [high], btype='high')
    y = lfilter(b, a, data)
    return y