""" A Simulator for the 'open_bci_ganglion' module """
import time

class OpenBCIBoard():
    def __init__(self):
        self.streaming = True

    def start_streaming(self, callback, duration=1):
        self.streaming = True
        timeout = time.time() + duration * 60
        signal = [1, 2, 3, 4]
        while time.time() < timeout and self.streaming:
            callback(signal)
            # Pause for 1 / frequency
            time.sleep(1 / 200)

    def stop(self):
        self.streaming = False



def test():
    board = OpenBCIBoard()
    board.start_streaming(handle_sample)

def handle_sample(sample):
    print(sample)
