import time
import matplotlib.pyplot as plt
import json



def saveFile():
    """Save List to file"""
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

saveFile()