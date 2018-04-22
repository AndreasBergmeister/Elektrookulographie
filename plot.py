import matplotlib.pyplot as plt

def plot_channels(signal):
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
        
        # Get the time-voltage graph for each channel
        graph = {'x': [], 'y': []}
        graph['x'] = times
        graph['y'] = channel 

        # Format the graph if the signal is 'advanced' (directions were recorded)
        if directions:
            # Color for each direction
            colors = {'0': 'b', 'up': 'r', 'down': 'g', 'right': 'c', 'left': 'm'}
            # Split the graph for each direction into a section
            graph_section = {'x': [], 'y': []}
            for j, (value, time, direction) in enumerate(zip(graph, times, directions)):
                graph_section['x'].append(time)
                graph_section['y'].append(value)
                # Plot graph section if the last value is reached or if the direction changes
                if j == len(directions) or directions[j] == directions[j + 1]:
                    plt.plot(graph_section['x'], graph_section ['y'], colors[direction])
                    # Empty the graph lists
                    graph_section = {'x': [], 'y': []}
        else:
            plt.plot(graph['x'], graph['y'])

        # Format the subplot
        plt.xlabel('t (s)')
        # plt.suptitle('Channel ' + str(i))
        plt.ylabel('U (V)')
        plt.title('Channel ' + str(i))
        # plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.8, wspace=0.35)
        plt.subplots_adjust(hspace=0.8)
    plt.show()