from statistics import mean
from open_bci_ganglion import OpenBCIBoard
# from open_bci_ganglion_simulator import OpenBCIBoard

"""Record as long as "Ctrl-C" is not pressed"""
board = OpenBCIBoard()
print('Start streaming')

# Calibrate
print('Calibrate start')
values = []
def calibrate(sample):
    values.append(sample.channel_data[0])
board.start_streaming(calibrate, 5)

values = [abs(x) for x in values]
voltage_blink = 2/3*max(values)
print('calibrate Finished')


blinks = 0
print('start testing')
def handle_sample(sample):
    """Callbackfunction appending the voltage of each channel (sample) and the time to the 'Signal'-object"""
    voltage = abs(sample.channel_data[0])
    if voltage >  voltage_blink:
        global blinks
        blinks += 1
        print(blinks)

try:
    board.start_streaming(handle_sample)
except KeyboardInterrupt:
    board.stop()