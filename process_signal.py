from scipy.interpolate import interp1d
import numpy as np
from matplotlib import pyplot as plt

def interpolate(x, y, frequency):
    # Calculate periodical x array with specific length
    length = x[-1]
    samples_amount = int(length * frequency)
    period_length = 1 / frequency    
    x_new = [period_length * i for i in range(samples_amount) if period_length * i >= x[0]]

    # Calculate interpolated y values
    y_new = [interp1d(x, y)(i) for i in x_new]

    return x_new, y_new

def fft(x, y):
    # Get real amplitudes of FFT (only in postive frequencies)
    fft_vals = np.absolute(np.fft.rfft(y))

    # Get frequencies for amplitudes in Hz
    dt = x[1] - x[0]
    fft_freq = np.fft.rfftfreq(len(y), dt)

    return fft_freq, fft_vals

    # # Plot
    # plt.plot(fft_freq, fft_vals)
    # plt.show()