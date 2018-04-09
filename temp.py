import json
import time

# Save list to file
saved_data_filename = ''
def get_filename():
    saved_data_filename = time.strftime("%Y%m%d-%H%M%S")
    name = input('Input filename: ')
    if(name):
        saved_data_filename += '_' + name + '_'
    saved_data_filename += '.txt'
    print(saved_data_filename)
    

# get_filename()
# saved_data_filename = time.strftime("%Y%m%d-%H%M%S")
# name = input('Input filename: ')
# if(name): 
#     saved_data_filename += '_' + name + '_'
# saved_data_filename += '.txt'

saved_data_filename = time.strftime("%Y%m%d-%H%M%S")
name = input('Input filename: ')
if(name):
    saved_data_filename += '_' + name + '_'
saved_data_filename += '.txt'
print(saved_data_filename)


with open(saved_data_filename, 'w') as file:
    json.dump('Hallo', file)