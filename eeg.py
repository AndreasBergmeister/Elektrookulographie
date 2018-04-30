import argparse
import file
import process_signal
from matplotlib import pyplot as plt

# Arparser
parser = argparse.ArgumentParser()
parser.add_argument('name')
args = parser.parse_args()
name = args.name

signal = file.get_signal(name)

x = signal['times']
y = signal['channels'][0]

xn, yn = process_signal.interpolate(x, y, 200)
xf, yf = process_signal.fft(xn,yn)
plt.plot(xf, yf)
plt.show()



