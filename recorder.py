import time

from open_bci_ganglion_simulator import OpenBCIBoard

class Recorder():
    """Records and saves data"""

    def __init__(self, channels_amount=4):
        self.channels_amount = channels_amount
        self.board = OpenBCIBoard()
        self.channels_amount = channels_amount

        self.signal = None
        self.current_direction = None


    def start_recording(self):
        """Record as long as "Ctrl-C" is not pressed"""
        self.signal = Signal(self.channels_amount)
        try:
            self.board.start_streaming(self.handle_sample)
        except KeyboardInterrupt:
            self.board.stop()

    def start_recording_advanced(self, duration, iterations):
        """ 
        Record several intervalls for a specific duration
        An intervall is the user's eye moving to all four directions 
        The duration the the time the eye persists in one direction
        Direction "0" = looking strait ahead
        """
        self.signal = SignalAdvanced(self.channels_amount)
        directions = ['0', 'up', '0', 'down', '0', 'left', '0', 'right']
        for _ in range(0, iterations):
            for direction in directions:
                print(direction)
                self.current_direction = direction
                self.board.start_streaming(self.handle_sample_advanced, duration)

    def handle_sample(self, sample):
        """Callbackfunction appending the signals of each channel to its apropiate list"""
        for i in range(self.channels_amount):
            self.signal.channels[i].append(sample[i])

    def handle_sample_advanced(self, sample):
        """Callbackfunction appending the signals of each channel, the direction and time to there apropiate lists"""
        self.handle_sample(sample)
        # Append the direction to its list
        self.signal.direction.append(self.current_direction)


    def get_signal(self):
        """Returns the created Signal object"""
        return self.signal


class Signal():
    """Stores the Signal of each channel"""

    def __init__(self, channels_amount):
        # Create list containing a list (=Signal) for each channel
        self.channels = []
        for _ in range(channels_amount):
            self.channels.append([])


class SignalAdvanced(Signal):
    """Stores the Signal of each channel and the direction that the eye is pointing at a specific time"""

    def __init__(self, channels_amount):
        super(channels_amount)

        self.direction = []
        self.time = []