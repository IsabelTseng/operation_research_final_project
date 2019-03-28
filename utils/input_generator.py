from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

def get_input():
    output = []
    total = 0
    time = 0

    #1~1800 seconds
    sample = np.random.poisson(0.05, size = 1800)
    noise = np.random.poisson(0.0167, size = 1800)
    floor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for i in sample:
        time = time + 1
        if i != 0:
            for j in range(i):
                total = total + 1
                data = {
                    'id': total,
                    'enter_floor': np.random.randint(2, 13),
                    'exit_floor': 1,
                    'time_quantum': np.random.randint(60, 301),
                    'timestamp': time,
                    'direction': -1
                }
                output.append(data)
        if noise[time - 1] != 0:
            for j in range(noise[time - 1]):
                total = total + 1
                path = np.random.choice(floor, size = 2, replace = False)
                data = {
                    'id': total,
                    'enter_floor': path[0],
                    'exit_floor': path[1],
                    'time_quantum': np.random.randint(60, 301),
                    'timestamp': time,
                    'direction': np.sign(path[1] - path[0])
                }
                output.append(data)

    #1801~3600 seconds
    sample = np.random.poisson(0.05, size = 1800)
    noise = np.random.poisson(0.0167, size = 1800)
    for i in sample:
        time = time + 1
        if i != 0:
            for j in range(i):
                total = total + 1
                data = {
                    'id':total,
                    'enter_floor': 1,
                    'exit_floor': np.random.randint(2, 13),
                    'time_quantum': np.random.randint(60, 301),
                    'timestamp': time,
                    'direction': 1
                }
                output.append(data)
        if noise[time - 1801] != 0:
            for j in range(noise[time - 1801]):
                total = total + 1
                path = np.random.choice(floor, size = 2, replace = False)
                data = {
                    'id': total,
                    'enter_floor': path[0],
                    'exit_floor': path[1],
                    'time_quantum': np.random.randint(60, 301),
                    'timestamp': time,
                    'direction': np.sign(path[1] - path[0])
                }
                output.append(data)
    print(total)
    return output