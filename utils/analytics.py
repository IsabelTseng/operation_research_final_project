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