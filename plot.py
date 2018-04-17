import matplotlib.pyplot as plt

def plot_channels(signal):
    """Plot the graph of the signal for each channel"""

    for channel in signal.channels:
        # Get the time-voltage graph for each channel
        graph = {'x': [], 'y': []}
        graph['x'] = signal.time
        graph['y'] = channel
        
        # Plot each channel as subplot
        plt.subplot(len(signal.channels))

        # Format the graph if the signal has a direction list
        if signal.directions:
            # Color for each direction
            colors = {'0': 'b', 'up': 'r', 'down': 'g', 'right': 'c', 'left': 'm'}
            # Split the graph for each direction into a section
            graph_section = {'x': [], 'y': []}
            for i, value, time, direction in enumerate(zip(graph, signal.time, signal.directions)):
                graph_section['x'].append(time)
                graph_section['y'].append(value)
                # Plot graph section if the last value is reached or if the direction changes
                if i == len(signal.directions) or signal.directions[i] == signal.directions[i + 1]:
                    plt.plot(graph_section['x'], graph_section ['y'], colors[direction])
                    graph_section.clear()
        else:
            plt.plot(graph['x'], graph['y'])

        # Format the subplot
        plt.xlabel('Time (s)')
        plt.title('Channel ' + i + 1)
        plt.ylabel('Amplitude (V)')

    plt.show()