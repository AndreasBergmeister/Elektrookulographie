import time
import json
import asyncio

# from open_bci_ganglion import OpenBCIBoard
from open_bci_ganglion_simulator import OpenBCIBoard

def record(channels_amount=4):
    """Record as long as "Ctrl-C" is not pressed"""
    board = OpenBCIBoard()
    signal = signal_dictionary(channels_amount)
    print('Start streaming')
    start_recording_time = time.perf_counter()

    def handle_sample(sample):
        """Callbackfunction appending the voltage of each channel (sample) and the time to the 'Signal'-object"""
        signal['times'].append(time.perf_counter() - start_recording_time)
        for i in range(channels_amount):
            signal['channels'][i].append(sample.channel_data[i])

    try:
        board.start_streaming(handle_sample)
    except KeyboardInterrupt:
        board.stop()
        return signal


def record_advanced(duration, iterations, channels_amount=4):
    board = OpenBCIBoard()
    signal = signal_dictionary(channels_amount)
    directions = ['0', 'up', '0', 'down', '0', 'right', '0', 'left', '0'] * iterations
    # Time when change direction 
    direction_change_time = [i*duration for i in len(directions)]
    # Current time
    start_recording_time = time.perf_counter()
    finish_recording_time = start_recording_time + len(directions) * duration

    def handle_sample(sample):
        time_now = time.perf_counter() - start_recording_time
        # Finish recording if time is over
        if time_now > finish_recording_time:
            board.stop()
            return
        
        # Append time to its list
        signal['times'].append(time_now)

        # Append each channels value to its list
        for i in range(channels_amount):
            signal['channels'][i].append(sample.channel_data[i])

        # Calculate the current direction by time
        direction = None        
        for i in direction_change_time:
            if i == len(direction_change_time) -1 or (time_now >= direction_change_time[i] and time_now < direction_change_time[i+1]):
                direction = directions[i]
                break
        
        # Print direction if it changed
        if direction is not direction[-1]:
            print(direction)

        # Append the direction to its list
        signal['directions'].append(direction)


    print('Start streaming')
    board.start_streaming(handle_sample)
    print('Stopped streaming')
    return signal       


def signal_dictionary(channels_amount):
    signal = {
        'channels': [],
        'times': [],
        'directions': []
    }

    # Add a list for each channel to channels
    signal['channels'] = [[] for _ in range(channels_amount)]

    return signal