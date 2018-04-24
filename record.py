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
    """ 
    Record several intervalls for a specific duration.
    An intervall is the user's eye moving to all four directions.
    The duration the the time the eye persists in one direction.
                            
    Direction "0" = looking strait ahead
    """
    board = OpenBCIBoard()
    signal = signal_dictionary(channels_amount)
    directions = ['0', 'up', '0', 'down', '0', 'right', '0', 'left', '0']
    print('Start streaming')      
    start_recording_time = time.perf_counter()   
    for _ in range(0, iterations):
        for direction in directions:
            print(direction)

            def handle_sample(sample):
                """Callbackfunction appending the voltage of each channel (sample), the time and the direction to the 'Signal'-object"""
                signal['times'].append(time.perf_counter() - start_recording_time)
                for i in range(channels_amount):
                    signal['channels'][i].append(sample.channel_data[i])
                # Append the direction to its list
                signal['directions'].append(direction)

            board.start_streaming(handle_sample, duration)

    board.stop()
   
   
    return signal

    async def recording():
        for _ in range(0, iterations):
            for direction in directions:
                print(direction)
                await asyncio.sleep(duration)
                # Fill direction list with the current direction
                signal['directions'] = [direction for _ in range(len(signal['directions'], len(signal['times'])))]

def signal_dictionary(channels_amount):
    signal = {
        'channels': [],
        'times': [],
        'directions': []
    }

    # Add a list for each channel to channels
    signal['channels'] = [[] for _ in range(channels_amount)]

    return signal