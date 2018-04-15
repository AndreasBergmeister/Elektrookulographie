import time

from open_bci_ganglion_simulator import OpenBCIBoard
from signal import Signal




def record(channels_amount):
    """Record as long as "Ctrl-C" is not pressed"""
    board = OpenBCIBoard()
    signal = Signal(channels_amount)
    start_recording_time = time.perf_counter()
    try:
        board.start_streaming(handle_sample)
    except KeyboardInterrupt:
        board.stop()
        return signal

    def handle_sample(sample):
        """Callbackfunction appending the voltage of each channel (sample) and the time to the 'Signal'-object"""
        signal.time.append(time.perf_counter() - start_recording_time)
        for i in range(channels_amount):
            signal.channels[i].append(sample[i])


def record_advanced(channels_amount, duration, iterations):
        """ 
        Record several intervalls for a specific duration
        An intervall is the user's eye moving to all four directions 
        The duration the the time the eye persists in one direction
        Direction "0" = looking strait ahead
        """
        board = OpenBCIBoard()
        signal = Signal(channels_amount)
        start_recording_time = time.perf_counter()
        directions = ['0', 'up', '0', 'down', '0', 'right', '0', 'left']
        for _ in range(0, iterations):
            for direction in directions:
                print(direction)
                board.start_streaming(handle_sample, duration)

                def handle_sample(sample):
                    """Callbackfunction appending the voltage of each channel (sample), the time and the direction to the 'Signal'-object"""
                    signal.time.append(time.perf_counter() - start_recording_time)
                    for i in range(channels_amount):
                        signal.channels[i].append(sample[i])
                    # Append the direction to its list
                    signal.direction.append(direction)