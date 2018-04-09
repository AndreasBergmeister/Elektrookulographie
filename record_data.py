import time
import matplotlib.pyplot as plt
import json

from open_bci_ganglion import OpenBCIBoard

# List containing Lists for each channel
data = []

# Append 4 Lists (4 channels) to the list
for i in range(0, 3):
    data.append([])


# Recording signal
def handle_sample(sample):
    for i in range(0, 3):
        data[i].append(sample.channel_data[i])

board = OpenBCIBoard()
board.start_streaming(handle_sample, 5)


# Save list to file
def get_filename():
    filename = 'records/' + time.strftime("%Y%m%d-%H%M%S")
    name = input('Input filename: ')
    if(name):
        filename += '_' + name + '_'
    filename += '.txt'
    return filename

try:
    with open(get_filename(), 'w') as file:
        json.dump(data, file)
except Exception as e:
    print(e)
else:
    print('Record successfully saved.')