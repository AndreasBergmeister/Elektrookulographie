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
signal = file.get_signal('20180429-213420_Maria_gd_blink_.json')

x = signal['times']
y = signal['channels'][0]


xn, yn = process_signal.interpolate(x, y, 200)

yn_filtered = process_signal.butter_bandpass_filter(yn, 0.5, 5, 200)

plt.plot(xn, yn, color='blue')
plt.plot(xn, yn_filtered, color='red')

plt.show()