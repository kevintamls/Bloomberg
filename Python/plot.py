from Q3 import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def runSimulation(alpha, beta):
    trialresults1 = []
    avgtrialresults1 = []
    trialresults2 = []
    avgtrialresults2 = []
    
    for i in range(10000):
        trialresults1.append(singleQueue(alpha, beta))
        trialresults2.append(doubleQueue(alpha, beta))
        avg1 = sum(trialresults1) / float(len(trialresults1))
        avg2 = sum(trialresults2) / float(len(trialresults2))
    return(avg1, avg2)
        



x = np.arange(1, 11, 1)
ya1 = [37.7819, 5.4515000000000002, 4.0347999999999997, 3.3782999999999999, 2.9577, 2.6762000000000001, 2.4891999999999999, 2.3452999999999999, 2.2360000000000002, 2.1572]   
ya07 = [12.903, 7.2679, 4.9340000000000002, 3.9651000000000001, 3.4264000000000001, 3.0764999999999998, 2.8109000000000002, 2.6111, 2.4679000000000002, 2.3555000000000001]
ya05 = [8.2779000000000007, 4.4663000000000004, 3.4603000000000002, 2.9495, 2.6366000000000001, 2.4155000000000002, 2.2650000000000001, 2.1745000000000001, 2.0754999999999999, 2.0043000000000002]
ya03 = [5.5186999999999999, 3.5215999999999998, 2.8626999999999998, 2.4832000000000001, 2.2772000000000001, 2.1459000000000001, 2.0482999999999998, 1.9614, 1.8671, 1.7927999999999999]   
yt1 = [7.7218, 3.1179, 2.3165, 1.9426, 1.7585, 1.6606, 1.5926, 1.5375, 1.4659, 1.3946]      

ya1_patch = mpatches.Patch(color='blue', label='Beta Value: 1')
ya07_patch = mpatches.Patch(color='orange', label='Beta Value: 0.7')
ya05_patch = mpatches.Patch(color='green', label='Beta Value: 0.5')
ya03_patch = mpatches.Patch(color='red', label='Beta Value: 0.3')
yt1_patch = mpatches.Patch(color='purple', label='2 tellers')

plt.plot(x, ya1, x, ya07, x, ya05, x, ya03, x, yt1)
plt.xlabel('Mean Gap between customers arriving (mins)')
plt.ylabel('Average Max Queue Length')
plt.title('Alpha Value against Average Max Queue Length')
plt.legend(handles=[ya1_patch, ya07_patch, ya05_patch, ya03_patch, yt1_patch])
plt.show()

