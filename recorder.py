import time
import matplotlib.pyplot as plt
import json

from open_bci_ganglion_simulator import OpenBCIBoard

class Recorder():
    """  Records and saves data """

    def __init__(self, channels_amount=4):
        self.channels_amount = channels_amount
        self.board = OpenBCIBoard()
        self.singal = Signal(channels_amount)

    def start_recording(self):
        """ Record while "Ctrl-C" is not pressed """
        try:
            self.board.start_streaming(self.handle_sample)
        except KeyboardInterrupt:
            self.board.stop()

    def record(self, duration, iterations):
        """ 
        Record several intervalls for a specific duration
        An intervall is the user's eye moving to all four directions 
        The duration the the time the eye persists in one direction
        Direction "0" = looking strait ahead
        """
        directions = ['0', 'up', '0', 'down', '0', 'left', '0', 'right']
        for _ in range(0, iterations):
            for direction in directions:
                print(direction)
                self.direction = direction  # net sicho ob des geat!!!!!!!!!!!!!!!!!!
                self.board.start_streaming(self.handle_sample, duration)

    def handle_sample(self, sample):
        # Appned signals of each channel to its apropiate list
        for i, channel in enumerate(sample):
            self.singal.channels[i].append(channel)
        # Append the direction to its list
        self.singal.direction.append(self.direction)


class Signal():
    """Stores the Signal of each channel and the direction that the eye is pointing at a specific time"""

    def __init__(self, channels_amount, contains_time=True, contains_direction=True):
        # Create list containing a list (=Signal) for each channel
        self.channels = []
        for i in range(channels_amount):
            self.channels.append([])
        
        # List containing the direction the eye is looktin to
        if contains_direction:
            self.direction = []

        # List containing the time for each epoch
        if contains_time:
            self.time = []