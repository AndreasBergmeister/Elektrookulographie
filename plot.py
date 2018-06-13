"""Module for formated plotting the recorded signal"""

import matplotlib.pyplot as plt

import process_signal

def plot(signal):
    """Plot the graph of the signal for each channel"""
    # Extracting dictionary
    channels = signal['channels']
    times = signal['times']
    directions = signal['directions']

    # Plot each channel as subplot
    for i, channel in enumerate(channels):
        # Start index at 1
        i += 1
        # Create subplot
        plt.subplot(len(channels), 1, i)

        # Interpolate signal
        FREQUENCY = 200
        x, y = process_signal.resample(times, channel, FREQUENCY)

        # Filter signal
        y = process_signal.butter_lowpass_filter(y, 10, FREQUENCY)

        # Format the graph if the signal contains the directions (record_advanced)
        if directions:
            # Color for each direction
            colors = {'0': 'b', 'up': 'r', 'down': 'g', 'right': 'c', 'left': 'm'}
            # Split the graph for each direction into a section
            # Get the index for each direction change (direction change indexes)
            dc_indexes = [i for i in range(1, len(directions)) if directions[i] != directions[i-1]]
            # Get the time for each direction change (time change indexes)
            dc_times = [times[i] for i in dc_indexes]

            # Get and plot sections
            section_start = 0
            for dc_time, dc_index in zip(dc_times, dc_indexes):
                x_section = []
                y_section = []
                for time, value in zip(x, y):
                    if time >= section_start and time < dc_time:
                        x_section.append(time)
                        y_section.append(value)
                plt.plot(x_section, y_section, colors[directions[dc_index-1]])
                section_start = dc_time

        # Else plot the graph right away
        else:
            plt.plot(x, y)

        # Format the subplot
        plt.title('Channel ' + str(i))
        plt.xlabel('t (s)')
        plt.ylabel('U (μV)')
        plt.subplots_adjust(hspace=0.8)
    plt.show()