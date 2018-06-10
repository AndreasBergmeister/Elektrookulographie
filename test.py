# import record
# import plot
import file
import process_signal
from matplotlib import pyplot as plt
import json
import numpy
# signal = record.record_advanced(0.5,1)
# signal = record.record()


# file.print_signal(signal)
# plot.plot_channels(file.get_signal('records/2018042220180429-213008_Maria_gd_.json
FREQUENCY = 200

signal = file.get_signal('20180603-232127_advanced_.json')

x = signal['times']
y = signal['channels'][0]


xn, yn = process_signal.resample(x, y, FREQUENCY)

# yn_filtered = process_signal.butter_bandpass_filter(yn, 0.01, 1, FREQUENCY)
yn_filtered = process_signal.butter_highpass_filter(yn, 1, FREQUENCY)



# plt.plot(*process_signal.fft(x,y), color='red')
# plt.plot(*process_signal.fft(xn,yn), color='green')


plt.plot(xn, yn_filtered, color='red')
# plt.plot(xn, yn, color='blue')

plt.show()