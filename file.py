"""Module containing functions to save and load the signal using the JSON format"""

import json
import time
import os

DIRECTORY = 'records'

def get_filename(name):
    """Get the filename based on the current DateTime"""
    filename = time.strftime("%Y%m%d-%H%M%S")
    if name:
        filename += '_' + name + '_'
    filename += '.json'
    return os.path.join(DIRECTORY, filename)

def save_signal(signal, name):
    """
    Save the signal as a JSON-string to a file
    Returns the filename
    """
    filename = get_filename(name)
    with open(filename, 'w') as file:
        json.dump(signal, file)
    return filename

def get_signal(filename):
    """
    Load a JSON file as a string
    Returns the parsed object
    """
    with open(os.path.join(DIRECTORY, filename)) as file:
        return json.load(file)

def print_signal(signal):
    """Load a JSON file and print it as a string"""
    print(json.dumps(signal, indent=4))