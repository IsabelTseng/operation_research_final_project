import matplotlib.pyplot as plt
import numpy as np

def get_histogram(data, title, xlabel, ylabel, filename, bins):
    plt.hist(data, bins)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(f"image/{ filename }.png")
    plt.close()