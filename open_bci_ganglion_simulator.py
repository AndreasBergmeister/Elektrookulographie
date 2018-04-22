""" A Simulator for the 'open_bci_ganglion' module """
import time

class OpenBCIBoard():
    def __init__(self):
        self.streaming = True

    def start_streaming(self, callback, duration=1000):
        self.streaming = True
        timeout = time.perf_counter() + duration
        signal = [1, 2, 3, 4]
        while time.perf_counter() < timeout and self.streaming:
            callback(signal)
            # Pause for 1 / frequency
            time.sleep(1 / 200)

    def stop(self):
        self.streaming = False



def test():
    board = OpenBCIBoard()
    start_time = time.perf_counter()
    board.start_streaming(handle_sample)
    print(time.perf_counter() - start_time)

def handle_sample(sample):
    print(sample)