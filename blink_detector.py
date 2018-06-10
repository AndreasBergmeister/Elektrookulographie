"""Module for detecting blinks in a recorded signal"""

from matplotlib import pyplot as plt

import process_signal
import file

def detect(signal):
    x = signal['times']
    y = signal['channels'][0]

    # Resample Signal
    FREQUENCY = 100
    x, y = process_signal.resample(x, y, FREQUENCY)

    # Filter Signal
    LOWCUT = 2
    HIGHCUT = 5
    y_filtered = process_signal.butter_bandpass_filter(y, LOWCUT, HIGHCUT, FREQUENCY)

    # Detect peaks
    def detect_peaks(y):
        """Get indices all peaks"""
        # Peak: value has to be greater than previous and following value
        peaks = [i for i in range(1, len(y) - 1) if y[i] > y[i-1] and y[i] > y[i+1]]
        
        # Get minimum peak height
        mph = max(y) * 0.75 # Minimum peak hight
        
        # Get peaks greater than minimum-peak-height
        peaks = [peak for peak in peaks if y[peak] >= mph]
        return peaks

    peaks_indexes = detect_peaks(y_filtered)
    print('Detected blinks: ' + str((len(peaks_indexes))))

    # Plot filtered Signal with peaks
    for peak_index in peaks_indexes:
        plt.plot(x[peak_index], y_filtered[peak_index], 'ro')

    plt.plot(x, y_filtered, color='blue')
    plt.show()