import matplotlib.pyplot as plt
import json

# Load file to list
saved_data_filename = 'record.txt'
with open(saved_data_filename) as file:
    data = json.load(file)
print('Loaded File' + saved_data_filename)

# Printing Signal
print("Printing graph")
for i in range(0,3):
    # plt.plot(data[i])
    # plt.show()
    print(i)