from statistics import mean

from open_bci_ganglion import OpenBCIBoard
import process_signal

board = OpenBCIBoard()

minimum_blink_distance = 2
last_samples_amount = 1000

last_blink_time = 0
last_samples = []
blink_value = 0
blink_counter = 0
def handle_sample(sample):
    global last_blink_time
    global blink_counter
    global blink_value
    print(sample.channel_data[0])
    
    if sample.channel_data[0] > blink_value and sample.capturing_time > last_blink_time + minimum_blink_distance:
        blink_counter += 1
        last_blink_time = sample.capturing_time
        print('Blink ' + str(blink_counter))

    last_samples.append(sample.channel_data[0])
    # Limit list to fixed size
    if len(last_samples) > last_samples_amount:
        last_samples.pop(0)

    # Calculate new blink value
    last_samples_mean = mean(last_samples)
    blink_value = last_samples_mean + 2 * abs(last_samples_mean)



print('start testing')
try:
    board.start_streaming(handle_sample)
except KeyboardInterrupt:
    board.stop()