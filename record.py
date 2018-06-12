"""Module for simple and advanced streaming and recording from the Ganglion board"""

import time

from open_bci_ganglion import OpenBCIBoard

def record(channels_amount=4):
    """Record as long as "Ctrl-C" is not pressed"""
    board = OpenBCIBoard()
    signal = signal_dictionary(channels_amount)
    start_recording_time = 0

    def handle_sample(sample):
        """Callbackfunction appending the voltage of each channel (sample) and the time to the signal-dictionary"""
        # Set start_recording_time
        if not signal['times']:
            nonlocal start_recording_time
            start_recording_time = sample.capturing_time
        
        # Append time to it's list
        signal['times'].append(sample.capturing_time - start_recording_time)
        
        # Append each channels value to its list
        for i in range(channels_amount):
            signal['channels'][i].append(sample.channel_data[i])

    # Start streaming
    print('Start streaming')
    try:
        board.start_streaming(handle_sample)
    except KeyboardInterrupt:
        # Stop streaming
        board.stop()
        print('Stopped streaming')
        return signal


def record_advanced(duration, iterations, channels_amount=4):
    """
    The user is shown the direction in which he should look.
    The signal is recorded with the direction in which the user is looking at a specific time.
    """
    board = OpenBCIBoard()
    signal = signal_dictionary(channels_amount)
    directions = ['0', 'up', '0', 'down', '0', 'right', '0', 'left', '0'] * iterations
    direction_changes = len(directions)
    direction_change_times = [i*duration for i in range(direction_changes)]
    recording_duration = len(directions) * duration    
    start_recording_time = 0

    def handle_sample(sample):
        """Callbackfunction appending the voltage of each channel (sample), the time and the current direction to the signal-dictionary"""
        # Set start_recording_time        
        if not signal['times']:
            nonlocal start_recording_time
            start_recording_time = sample.capturing_time

        recording_time = sample.capturing_time - start_recording_time
        
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

    # Start streaming
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