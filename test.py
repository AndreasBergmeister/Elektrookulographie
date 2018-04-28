# import record
# import plot
import file
import process_signal
from matplotlib import pyplot
import json
import numpy
# signal = record.record_advanced(0.5,1)
# signal = record.record()


# file.print_signal(signal)
# plot.plot_channels(file.get_signal('records/20180422-160541_Test_.txt'))

signal = file.get_signal('20180426-220436_mama_simple_.json')

x = signal['times']
y = signal['channels'][0]


xn, yn = process_signal.interpolate(x, y, 200)

# print(json.dumps(xn, indent=4))
# pyplot.plot(xn, yn)
# pyplot.show()

process_signal.fft(xn,yn)
