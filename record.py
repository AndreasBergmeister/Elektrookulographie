import time
import json
import asyncio

from open_bci_ganglion import OpenBCIBoard
# from open_bci_ganglion_simulator import OpenBCIBoard

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
    direction_changes = len(directions)
    # Time when change direction 
    direction_change_times = [i*duration for i in range(direction_changes)]
    # Current time
    start_recording_time = time.perf_counter()
    recording_duration = len(directions) * duration

    def handle_sample(sample):      
        recording_time = time.perf_counter() - start_recording_time
        # Finish recording if time is over
        if recording_time > recording_duration:
            board.stop()
            return
        
        # Append time to its list
        signal['times'].append(recording_time)

        # Append each channels value to its list
        for i in range(channels_amount):
            signal['channels'][i].append(sample.channel_data[i])

        # Calculate the current direction by time
        for i, direction in enumerate(directions):
            if i == len(direction_change_times) -1 or (recording_time >= direction_change_times[i] and recording_time < direction_change_times[i+1]):
                # Print direction if it's the first one or if it changed
                if not signal['directions'] or direction != signal['directions'][-1]:
                    print(direction)

                # Append the direction to its list
                signal['directions'].append(direction)
                break

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