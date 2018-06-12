"""Module containing several functions for processing the signal"""

from scipy.interpolate import interp1d
from scipy.signal import butter, lfilter
import numpy as np
from matplotlib import pyplot as plt

def resample(x, y, frequency):
    # Calculate the new sample amount and the period length of one sample
    length = x[-1]
    samples_amount = int(length * frequency)
    period_length = 1 / frequency
    # Create list with x-values (time values) for the given frequency
    # First value has to be greater or equal the first value of the input
    x_new = [period_length * i for i in range(samples_amount) if period_length * i >= x[0]]
    
    # Calculate interpolated y values
    y_new = [interp1d(x, y)(i).tolist() for i in x_new]

    return x_new, y_new

def fft(y, frequency):
    # Get real amplitudes of FFT (only in positive frequencies)
    fft_values = np.absolute(np.fft.rfft(y))

    # Get frequencies for amplitudes in Hz
    dt = 1 / frequency
    fft_freq = np.fft.rfftfreq(len(y), dt)

    return fft_freq, fft_values

def butter_bandpass_filter(data, lowcut, highcut, frequency, order=1):
    nyq = 0.5 * frequency
    low = lowcut / nyq
    high = highcut / nyq

    b, a = butter(order, [low, high], btype='band')
    return lfilter(b, a, data)

def butter_highpass_filter(data, highcut, frequency, order=1):
    nyq = 0.5 * frequency
    high = highcut / nyq

    b, a = butter(order, [high], btype='high')
    return lfilter(b, a, data)