import matplotlib.pyplot as plt
import numpy as np

def get_average(data):
    return int(np.average(data))

def get_std(data):
    return round(np.std(data), 2)

def get_histogram(data, title, xlabel, ylabel, filename, x_min, x_max, bins):
    plt.hist(data, bins)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xlim(x_min, x_max)
    plt.savefig(f"image/{ filename }.png")
    plt.close()

def pyramid_plot(y, data1, data1label, data2, data1labe2):
    fig, axes = plt.subplots(ncols=2, sharey=True)
#     data1 = np.arange(data1.size)
#     data2 = np.arange(data2.size)
    axes[0].barh(y, data1, align='center', color='red')
    axes[0].set(title = data1label)
    axes[1].barh(y, data2, align='center', color='blue')
    axes[1].set(title = data1labe2)
    axes[0].invert_xaxis()
    axes[0].yaxis.tick_right()
    plt.show()