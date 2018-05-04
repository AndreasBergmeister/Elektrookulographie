from statistics import mean
from scipy.signal import argrelextrema
from matplotlib import pyplot as plt

from detect_peaks import detect_peaks
import process_signal
import file

signal = file.get_signal('20180429-213420_Maria_gd_blink_.json')
# signal_x = signal['times']
# signal_y = signal['channels'][0]
# signal = {'channel_1': signal['channels'][0], 'times': signal['times']}

FREQUENCY = 100

# Restructure sample
samples = []
for value, time in zip(signal['channels'][0], signal['times']):
    sample = {'value': value, 'time': time}
    samples.append(sample)

# Split into epochs
epoch_length = 1
epochs = []
epoch = []
last_time = 0
for sample in samples:
    if sample['time'] < epoch_length + last_time:
        epoch.append(sample)
    else:
        epochs.append(epoch)
        epoch = []
        last_time = sample['time']

counter = 0
# Process epochs
for epoch in epochs:
    # Get signal
    x = []
    y = []
    for sample in epoch:
        x.append(sample['time'])
        y.append(sample['value'])        
    # Interpolate epoch
    x, y = process_signal.interpolate(x, y, FREQUENCY)
    

    # Detect peaks
    a = mean(y)
    mph = mean(y) + abs(mean(y)) # Minimum peak hight
    mpd = FREQUENCY * 0.2 # Minimum peak distance (in number of data)
    peaks_indexes = detect_peaks(y, mph, mpd).tolist()

    # Plot peaks
    for peak_index in peaks_indexes:
        plt.plot(x[peak_index], y[peak_index], 'bo')
    
    # Plot epoch
    plt.plot(x ,y)

plt.show()