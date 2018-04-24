import record
import plot
import file

print('Initializing')

# Configure record
duration = 0.5
iterations = 1
channels = 4
# signal = record.record_advanced(duration, iterations, channels)
signal = record.record()

print('Finished recording')

# Save Signal
file.save_signal(signal)

# Plot Signal
