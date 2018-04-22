import matplotlib.pyplot as plt

def plot_channels(signal):
    """Plot the graph of the signal for each channel"""

    for i, channel in enumerate(signal.channels):
        # Start index at 1
        i += 1
        # Get the time-voltage graph for each channel
        graph = {'x': [], 'y': []}
        graph['x'] = signal.times
        graph['y'] = channel
        
        # Plot each channel as subplot
        plt.subplot(len(signal.channels), 1, i)

        # Format the graph if the signal has a direction list
        if signal.directions:
            # Color for each direction
            colors = {'0': 'b', 'up': 'r', 'down': 'g', 'right': 'c', 'left': 'm'}
            # Split the graph for each direction into a section
            graph_section = {'x': [], 'y': []}
            for j, (value, time, direction) in enumerate(zip(graph, signal.times, signal.directions)):
                graph_section['x'].append(time)
                graph_section['y'].append(value)
                # Plot graph section if the last value is reached or if the direction changes
                if j == len(signal.directions) or signal.directions[j] == signal.directions[j + 1]:
                    plt.plot(graph_section['x'], graph_section ['y'], colors[direction])
                    # Empty the graph lists
                    graph_section = {'x': [], 'y': []}
        else:
            plt.plot(graph['x'], graph['y'])

        # Format the subplot
        plt.xlabel('Time (s)')
        plt.suptitle('Channel ' + str(i))
        plt.ylabel('Amplitude (V)')
    plt.subplots_adjust(wspace=1)
    plt.show()