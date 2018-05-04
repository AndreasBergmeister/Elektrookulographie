from statistics import mean
import numpy as np
from scipy.signal import argrelextrema

from open_bci_ganglion import OpenBCIBoard
# from open_bci_ganglion_simulator import OpenBCIBoard
import process_signal

board = OpenBCIBoard()

# Calibrate: Calculate 0 Voltage
print('Calibrate start')
values = []
def calibrate(sample):
    values.append(sample.channel_data[0])
board.start_streaming(calibrate, 5)

voltage_zero = mean(values)
print('Calibrate Finished')

last_index = 0
# Epoching
frequency = 200
epoch_lenght = 0.5
epoch_size = int(frequency * epoch_lenght)

signal = {
        'channel_data': [],
        'capturing_time': []
    }

def handle_sample(sample):
    signal['channel_data'].append(sample.channel_data[0] - voltage_zero)
    signal['capturing_time'].append(sample.capturing_time)
    
    nonlocal last_index
    if len(signal['channel_data']) >= epoch_size + last_index:
        # New last index
        last_index = len(signal['channel_data'])
        # Get Epoch
        x = signal['channel_data'][-epoch_size:]
        y = signal['capturing_time'][-epoch_size:]
        # Filter epoch
        x, y = process_signal.interpolate(x, y, frequency)
        y = process_signal.butter_bandpass_filter(y, 0.2, 5, 200)

        # Calculate local maxs
        local_maxs = argrelextrema(y, np.greater)
        local_maxs_mean = mean(local_maxs)

        # If one max is 2x as high as average --> blink
        for value in local_maxs:
            if value > local_maxs_mean * 2:
                print('Blink')

print('start testing')
try:
    board.start_streaming(handle_sample)
except KeyboardInterrupt:
    board.stop()