"""A Simulator for the 'open_bci_ganglion' module"""

import time

class OpenBCIBoard():
    def __init__(self):
        self.streaming = True

    def start_streaming(self, callback, duration=1000):
        self.streaming = True
        timeout = time.perf_counter() + duration
        signal = [1, 2, 3, 4]
        while time.perf_counter() < timeout and self.streaming:
            callback(OpenBCISample(signal))
            # Pause for 1 / frequency
            FREQUENCY = 200
            time.sleep(1 / FREQUENCY)

    def stop(self):
        self.streaming = False

class OpenBCISample():
    def __init__(self, signal):
        self.channel_data = signal