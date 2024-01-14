from names import letter_frequency, read_names
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_bar_graph(i):
    """ 
    Used to create animated bar graph.  Takes an integer, i, which represents 
    how many years into the data collection we are interested in. 
    DO NOT MODIFY THIS FUNCTION!
    """
    # x-values
    x = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # y-values
    y = letter_frequency(year_db, 1880+i)

    ax.clear()
    ax.bar(x, y, width = .5)
    ax.set_title(str(1880+i))
    ax.set_ylim([0,600000])


if __name__ == "__main__":

    # Read the names data.
    year_db = read_names('data/namesDataAll.csv')
    
    # # DO NOT MODIFY THE CODE BELOW
    # # create the figure and axes objects
    fig, ax = plt.subplots()
    ax.set_ylim([0,600000])
    plt.title('First Letter Frequency over Time')
    plt.xlabel('Letter')
    plt.ylabel('Frequency')

    # # run the animation
    ani = FuncAnimation(fig, animate_bar_graph, frames=142, interval=300, repeat=False)
    plt.show()
    