import json
import time
import os

def save_signal(signal, name):
    """
    Saves the signal as a json-string to a file
    Returns the filename
    """
    filename = get_filename(name)
    with open(filename, 'w') as file:
        json.dump(signal, file)
    return filename

def get_signal(filename):
    with open(filename) as file:
        return json.load(file)

def get_filename(name):
    """Loads the json-string from a file and retruns the object"""
    directory = 'records'
    filename = time.strftime("%Y%m%d-%H%M%S")
    if name:
        filename += '_' + name + '_'
    filename += '.json'
    return os.path.join(directory, filename)

def print_signal(signal):
    print(json.dumps(signal, indent=4))