from statistics import mean
from scipy.signal import argrelextrema
from matplotlib import pyplot as plt

from detect_peaks import detect_peaks
import process_signal
import file

signal = file.get_signal('20180429-212736_Maria_gd_.json')

FREQUENCY = 100

# Restructure sample
samples = []
for value, time in zip(signal['channels'][0], signal['times']):
    sample = {'value': value, 'time': time}
    samples.append(sample)

# Split into epochs
epoch_length = 1 # in seconds
epochs = []
epoch = []
last_time = 0
for sample in samples:
    # Append sample to current epoch if epoch is shorter than epoch length
    if sample['time'] < epoch_length + last_time:
        epoch.append(sample)
    # Else append current epoch to epochs-list and clear it
    else:
        epochs.append(epoch)
        epoch = []
        last_time = sample['time']

# Process epochs
counter = 0
for epoch in epochs:
    # Get signal
    x = []
    y = []
    for sample in epoch:
        x.append(sample['time'])
        y.append(sample['value'])        
    # Resample epoch
    x, y = process_signal.resample(x, y, FREQUENCY)

    # Detect peaks
    a = mean(y)
    mph = mean(y) + abs(mean(y)) # Minimum peak height
    mpd = FREQUENCY * 0.2 # Minimum peak distance (in number of data)
    peaks_indexes = detect_peaks(y, mph, mpd).tolist()

    # Plot peaks
    for peak_index in peaks_indexes:
        plt.plot(x[peak_index], y[peak_index], 'bo')
    
    # Plot epoch
    plt.plot(x ,y)

plt.show()