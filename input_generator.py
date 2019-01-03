from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np
def gen():
    output = []
    total = 0
    time = 0
    
    #1~1800 seconds
    sample = np.random.poisson(0.36, size=1800)
    for i in sample:
        time = time + 1
        if i==1:
            total = total + 1
            data = {
                'id':total,
                'enter_floor':np.random.randint(2,13),
                'exit_floor':1,
                'time_quantum':np.random.randint(60,301),
                'intime':time
            }
            output.append(data)

    #1801~3600 seconds
    sample = np.random.poisson(0.36, size=1800)
    for i in sample:
        time = time + 1
        if i==1:
            total = total + 1
            data = {
                'id':total,
                'enter_floor':1,
                'exit_floor':np.random.randint(2,13),
                'time_quantum':np.random.randint(60,301),
                'intime':time
            }
            output.append(data)
   
    print(total)
    return output