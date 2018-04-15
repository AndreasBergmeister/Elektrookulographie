import matplotlib.pyplot as plt

class SignalPlotter():

    def __init__(self, signal):
        self.signal = signal


    def plot_channels(self):
        graphs = self.get_graphs()
        graphs_amount = len(graphs)
        for i, graph in enumerate(graphs):
            plt.subplot(graphs_amount, 1, i)
            plt.plot(graph.x, graph.y)
            plt.title('Channel ' + i + 1)
            plt.xlabel('Time (s)')
            plt.ylabel('Amplitude (V)')

    def plot_channels_formatted(self):
        """Plot the graph of the signal for each channel"""
        graphs = self.get_graphs()
        graphs_amount = len(graphs)

        # Plot each graph as a subplot
        for i, graph in enumerate(graphs):
            plt.subplot(graphs_amount, 1, i)

            # Format the graph if the signal has a direction attribute
            if self.signal.direction is not None:
                # Split the graph into different sections (each direction has it own color)
                graph_section = Graph([], [])
                colors = {'0': 'b', 'up': 'r', 'down': 'g', 'right': 'c', 'left': 'm'}

                # Iterate 
                for j, value in enumerate(graph):
                    graph_section.add_point(self.signal.time[j], value)
                    
                    if j == len(graph) or self.signal.direction[j] == self.signal.direction[j + 1]:
                        plt.plot(graph_section.x, graph_section.y, colors[self.signal.direction[j]])
                        graph_section = Graph([], [])

            
            
            plt.plot(graph.x, graph.y)
            plt.xlabel('Time (s)')
            plt.title('Channel ' + i + 1)
            plt.ylabel('Amplitude (V)')

    def get_graphs(self):
        """Returns a list containing the graph for each channel"""
        graphs = []
        for channel in self.signal.channels:
            graphs.append(Graph(self.signal.time, channel))
        return graphs

    def format_graph(graph)

    
class Graph():
    """Contains lists for the x-values (time) and y-values (voltage) of a signal of the channel"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_point(self, x, y):
        self.x.append(x)
        self.y.append(y)


# Load file to list
saved_data_filename = 'record.txt'
with open(saved_data_filename) as file:
    data = json.load(file)
print('Loaded File' + saved_data_filename)

# Printing Signal
print("Printing graph")
for i in range(0,3):
    # plt.plot(data[i])
    # plt.show()
    print(i)