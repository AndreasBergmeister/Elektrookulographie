import record
import plot

signal = record.record_advanced(0.5,1)

print('signal recorded')

import plot
plot.plot_channels(signal)