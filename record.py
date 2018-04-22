import time

from open_bci_ganglion_simulator import OpenBCIBoard
# from sig import Sig


def record(channels_amount=4):
    """Record as long as "Ctrl-C" is not pressed"""
    board = OpenBCIBoard()
    # signal = Sig(channels_amount)
    signal = signal_dictionary(channels_amount)

    start_recording_time = time.perf_counter()

    def handle_sample(sample):
        """Callbackfunction appending the voltage of each channel (sample) and the time to the 'Signal'-object"""
        signal['times'].append(time.perf_counter() - start_recording_time)
        for i in range(channels_amount):
            signal['channels'][i].append(sample[i])

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
        # Add list attribute to signal
        start_recording_time = time.perf_counter()
        directions = ['0', 'up', '0', 'down', '0', 'right', '0', 'left', '0']
        for _ in range(0, iterations):
            for direction in directions:
                print(direction)

                def handle_sample(sample):
                    """Callbackfunction appending the voltage of each channel (sample), the time and the direction to the 'Signal'-object"""
                    signal['times'].append(time.perf_counter() - start_recording_time)
                    for i in range(channels_amount):
                        signal['channels'][i].append(sample[i])
                    # Append the direction to its list
                    signal['directions'].append(direction)

                board.start_streaming(handle_sample, duration)

        return signal

def signal_dictionary(channels_amount):
    signal = {
        'channels': [],
        'times': [],
        'directions': []
    }

    for _ in range(channels_amount):
        signal['channels'].append([])

    return signal