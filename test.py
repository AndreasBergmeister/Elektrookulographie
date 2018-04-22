import record
import plot

signal = record.record_advanced(0.5,1)
# signal = record.record()

print('signal recorded')

import plot
plot.plot_channels(signal)