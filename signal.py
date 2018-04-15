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