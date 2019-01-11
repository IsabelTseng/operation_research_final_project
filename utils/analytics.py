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

def get_multibarhplot(data1, legend1, data2, legend2, title, xlabel, ylabel, filename, bin_tags):
    index = np.arange(len(bin_tags))
    bin_width = 0.5
    plt.title(title)
    p1 = plt.barh(index, data1, bin_width, color = 'C0')
    p2 = plt.barh(index + bin_width, data2, bin_width, color = 'C1')
    plt.yticks(index + 1.5 * bin_width, bin_tags)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend((p1[0], p2[0]), (legend1, legend2))
    plt.savefig(f"image/{ filename }.png")
    plt.close()
