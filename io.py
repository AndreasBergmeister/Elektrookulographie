import json
import time

def save_signal(siganl):
    """Saves the signal as a json-string to a file"""
    with open(get_filename(), 'w') as file:
        json.dump(siganl, file)

def get_signal(filename):
    with open(filename) as file:
        return json.load(file)


def get_filename():
    """Loads the json-string from a file and retruns the object"""
    filename = time.strftime("%Y%m%d-%H%M%S")
    name = input('Input filename: ')
    if(name):
        filename += '_' + name + '_'
    filename += '.txt'
    return filename