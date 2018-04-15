import time
import pickle

from recorder import Recorder

recorder = Recorder(4)
recorder.start_recording_advanced(3, 2)
signal = recorder.get_signal()

# Get filename
filename = time.strftime("%Y%m%d-%H%M%S")
name = input('Input filename: ')
if(name):
    filename += '_' + name + '_'
directory = 'records/' + filename

def save_signal_pickle():
    """Save signal object to a pickle file"""
    with open(directory + filename + '.p') as file:
        pickle.dump(signal, file)

def save_signal_csv():
    """Save signal object to a csv file"""
