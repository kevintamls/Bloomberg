# -*- coding: utf-8 -*-
import random
import math
import csv
import matplotlib.pyplot as plt
import numpy as np


def nextTime(mean):
    return -mean * math.log(1 - random.random())

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

def doubleQueue(alpha, beta, time=480):
    c = 0
    ta = 0
    ts1 = 0
    ts2 = 0
    Q1 = 1
    Q2 = 0
    maxQ = 0
    counter = 1
    counter2 = 0

    while c < time:
        if ta < ts1 and ta < ts2:
            if Q1 > Q2:
                ts2 = ts2 - ta
                c = c + ta
                Q2 = Q2 + 1
                counter2 += 1
                if Q2 > maxQ:
                    maxQ = Q2
                ta = nextTime(alpha)
            else:
                ts1 = ts1 - ta
                c = c + ta
                Q1 = Q1 + 1
                counter2 += 1
                if Q1 > maxQ:
                    maxQ = Q1
                ta = nextTime(alpha)
        else:
            if ts1 > ts2:
                ta = ta - ts2
                Q2 = Q2 - 1
                ts1 = ts1 - ts2
                ts2 = nextTime(beta)
            else:
                ta = ta - ts1
                Q1 = Q1 - 1
                ts2 = ts2 - ts1
                ts1 = nextTime(beta)
        if Q1 == 0 or Q2 == 0:
            if Q1 > Q2:
                c = c + ta
                Q2 = Q2 + 1
                counter2 += 1
                if Q2 > maxQ:
                    maxQ = Q2
                ta = nextTime(alpha)
            else:
                c = c + ta
                Q1 = Q1 + 1
                counter2 += 1
                if Q1 > maxQ:
                    maxQ = Q1
                ta = nextTime(alpha)
    return maxQ
                
                
                
                    