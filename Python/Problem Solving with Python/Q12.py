# -*- coding: utf-8 -*-
import random
import math
import csv
import matplotlib.pyplot as plt
import numpy as np


def nextTime(mean):
    return -mean * math.log(1 - random.random())


def theoreticalMeanQueueLength(alpha, beta):
    """
    >>> theoreticalMeanQueueLength(10, 2)
    0.25
    >>> theoreticalMeanQueueLength(5, 1)
    0.25
    >>> theoreticalMeanQueueLength(4, 2)
    1.0
    >>> theoreticalMeanQueueLength(5.5, 1.3)
    0.3095238095238095
    >>> theoreticalMeanQueueLength(5.5, 0)
    0.0
    >>> theoreticalMeanQueueLength(1, 1)
    -1
    >>> type(theoreticalMeanQueueLength(10, 2))
    <class 'float'>
    """
    # Add code here
    try:
        a= beta/alpha
        a1=a/(1-a)
        return a1
    except ZeroDivisionError:
        return -1

    


def checkMean(mean, iterations=10000):
    """
    >>> random.seed(57)
    >>> checkMean(5, 10)
    6.309113224728108
    >>> random.seed(57)
    >>> checkMean(5, 1000)
    4.973347344130324
    >>> random.seed(57)
    >>> checkMean(5, 100000)
    4.988076126529703
    >>> random.seed(57)
    >>> checkMean(195, 100000)
    194.53496893466047
    >>> random.seed(57)
    >>> checkMean(195)
    196.71853828860912
    >>> random.seed(57)
    >>> checkMean(31)
    31.273203522804728
    >>> type(checkMean(31, 5))
    <class 'float'>
    """
    # Add code here
    randomSum = 0
    for i in range(iterations):
        randomSum += nextTime(mean)
    return randomSum / iterations
    


def readExperimentParameters(filename):
    """
    >>> readExperimentParameters('experiments.csv')[0]
    (10, 2, 480)
    >>> len(readExperimentParameters('experiments.csv'))
    5
    >>> readExperimentParameters('experiments.csv')[3]
    (20, 2, 480)
    >>> readExperimentParameters('experiments.csv')[2]
    (20, 15, 240)
    >>> type(readExperimentParameters('experiments.csv')[1])
    <class 'tuple'>
    """
    # Add code here
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        returnList = []

        for row in csv_reader:
        
            for i in range(len(row)):
                row[i] = row[i].strip()
                try:
                    row[i] = int(row[i])
                except ValueError:
                    pass

            if row[3] == 'h':
                row[2] = row[2] * 60

            returnList.append(tuple(row[:-2]))

        return returnList
        
def singleQueue(alpha, beta, time=480):
    """
    >>> random.seed(57)
    >>> singleQueue(10, 3, 480)
    3
    >>> random.seed(101)
    >>> singleQueue(5, 3, 480)
    6
    >>> random.seed(101)
    >>> singleQueue(5, 3)
    6
    >>> random.seed(935)
    >>> singleQueue(10, 9, 280)
    10
    >>> type(singleQueue(10, 9, 280))
    <class 'int'>
    """
    # Add code here
    ta = 0
    ts = 0
    c = 0
    maxQ = 0
    Q = 1
    simTime = time
    
    while c < simTime:
        if ta<ts:
            ts = ts-ta
            c = c+ta
            Q = Q+1
            if Q > maxQ:
                maxQ = Q
            ta = nextTime(alpha)
            if Q == 0:
                c = c + ta
                Q = Q+1
                if Q > maxQ:
                    maxQ = Q
                ta = nextTime(alpha)
        else:
            ta = ta-ts
            c = c+ts
            Q = Q-1
            ts = nextTime(beta)
            
            if Q == 0:
                c = c + ta
                Q = Q+1
                if Q > maxQ:
                    maxQ = Q
                ta = nextTime(alpha)
    return maxQ
    
def q2():
    x = np.arange(1.1, 10.1, 0.1)
    y = theoreticalMeanQueueLength(x,1)
    plt.plot(x, y)
    plt.xlabel('Mean gap betwen customers arriving')
    plt.ylabel('Theoretical Mean Queue length')
    plt.title('Theoretical Mean Queue Length of Customers whilst mean time to serve customer is 1')
    plt.show()

q2() 
                
                
                
                    