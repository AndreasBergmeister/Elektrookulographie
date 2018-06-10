"""Module for detecting blinks in realtime from the stream from the Ganglion board"""

import time

from open_bci_ganglion import OpenBCIBoard
import process_signal

def detect_live():
    board = OpenBCIBoard()

    # Buffer
    BUFFER_SIZE = 500
    channel = []
    times = []

    # Start recording time (to calculate blink frequency)
    start_recording_time = time.perf_counter()

    # Amount of detected blinks
    blinks_amount = 0

    def handle_sample(sample):
        # Append sample to buffer
        channel.append(sample.sample.channel_data[0])
        times.append(sample.capturing_time)
        
        # Detect blinks in buffer if it contains more samples than BUFFER_SIZE
        if len(channel) >= BUFFER_SIZE:
            # Resample Signal
            FREQUENCY = 100 # Hz
            x, y = process_signal.resample(times, channel, FREQUENCY)

            # Filter Signal
            LOWCUT = 2
            HIGHCUT = 5
            y_filtered = process_signal.butter_bandpass_filter(y, LOWCUT, HIGHCUT, FREQUENCY)
            
            # Detect peaks
            def detect_peaks(y):
                """Get indices all peaks"""
                # Peak: value has to be greater than previous and following value
                peaks = [i for i in range(1, len(y) - 1) if y[i] > y[i-1] and y[i] > y[i+1]]
                
                # Get minimum peak height
                mph = max(y) * 0.75 # Minimum peak hight
                
                # Get peaks greater than minimum-peak-height
                peaks = [peak for peak in peaks if y[peak] >= mph]
                return peaks

            blinks_detected = len(detect_peaks(y_filtered))
            if blinks_detected > 0:
                global blinks_amount
                blinks_amount += blinks_detected
                dt = (time.perf_counter() - start_recording_time) / 60 # Minutes since start
                blink_frequency = blinks_amount / dt # Blinks per minute

                print('Detected Blinks: ' + str(blinks_detected))
                print('Total detected blinks: ' + str(blinks_detected))
                print('Blink frequency:' + str(blink_frequency) + ' [Blinks per minute]')
                
            # Clear buffer
            channel.clear()
            times.clear()

    # Start detecting blinks
    print('Start detecting blinks')
    try:
        board.start_streaming(handle_sample)
    except KeyboardInterrupt:
        board.stop()