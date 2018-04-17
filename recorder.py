"""
Module to record data from the 'OpenBCI Ganglion' board.
"""
import time

from open_bci_ganglion_simulator import OpenBCIBoard

class Recorder():
    """
    Recorder object
    
    The data is returned as a 'Signal' object, containing
    - a list containing
        - lists for the voltage over time of each channel
    - a list containing the time when each sample was captured

    When calling 'start_recording_advanced' the object additionally contains
        - a list of the direction in which the eye was looking at the time the sample was captured
    """

    def __init__(self, channels_amount=4):
        self.channels_amount = channels_amount
        self.board = OpenBCIBoard()
        self.channels_amount = channels_amount

        self.signal = None
        self.start_recording_time = None
        self.current_direction = None


    def start_recording(self):
        """Record as long as "Ctrl-C" is not pressed"""
        self.signal = Signal(self.channels_amount)
        self.start_recording_time = time.perf_counter()
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
        self.signal = Signal(self.channels_amount)
        self.start_recording_time = time.perf_counter()
        directions = ['0', 'up', '0', 'down', '0', 'right', '0', 'left', '0']
        for _ in range(0, iterations):
            for direction in directions:
                print(direction)
                self.current_direction = direction
                self.board.start_streaming(self.handle_sample_advanced, duration)

    def handle_sample(self, sample):
        """Callbackfunction appending the voltage of each channel (sample) and the time to the 'Signal'-object"""
        self.signal.time.append(time.perf_counter() - self.start_recording_time)
        for i in range(self.channels_amount):
            self.signal.channels[i].append(sample[i])

    def handle_sample_advanced(self, sample):
        """Callbackfunction appending the voltage of each channel (sample), the time and the direction to the 'Signal'-object"""
        self.handle_sample(sample)
        # Append the direction to its list
        self.signal.direction.append(self.current_direction)


    def get_signal(self):
        """Returns the created Signal object"""
        return self.signal


    def save_as_csv(self):
        """Saves the signal as csv file"""



class Signal():
    """Stores the Signal (Voltage and time) of each channel"""

    def __init__(self, channels_amount):
        # List containing a list for the samples of each channel
        self.channels = []
        for _ in range(channels_amount):
            self.channels.append([])

        # List containing the time when each sample was captured
        self.time = []
        # List (for advanced recording) containing the direction in which the eye was looking at the time the sample was captured
        self.direction = None