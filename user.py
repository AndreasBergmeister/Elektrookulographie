import record
import file

print('Initializing')

# Configure record
duration = 3
iterations = 1
channels = 1
signal = record.record_advanced(duration, iterations, channels)

print('Finished recording')

# Save Signal
file.save_signal(signal)