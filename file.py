import json
import time
import os

def save_signal(signal):
    """Saves the signal as a json-string to a file"""
    filename = get_filename()
    with open(filename, 'w') as file:
        json.dump(signal, file)
    print('Saved signal to: ' + filename)

def get_signal(filename):
    with open(filename) as file:
        return json.load(file)

def get_filename():
    """Loads the json-string from a file and retruns the object"""
    directory = 'records'
    filename = time.strftime("%Y%m%d-%H%M%S")
    name = input('Input filename: ')
    if(name):
        filename += '_' + name + '_'
    filename += '.txt'
    return os.path.join(directory, filename)

def print_signal(signal):
    print(json.dumps(signal, indent=4))