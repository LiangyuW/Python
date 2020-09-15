# -*- coding: utf-8 -*-

import numpy as np
import math
import random

def f(x):
     return (math.e**(-1*x))/(1+(x-1)**2)

# monte carlo estimation of integral of function f(x) over 
# the range (lower_bound, upper_bound)
def monte_carlo(num_samples, lower_bound, upper_bound):
    sum_of_samples=0
    for i in range(num_samples):
        x=random.uniform(lower_bound, upper_bound)
        sum_of_samples+=f(x)
    return (upper_bound-lower_bound)*float(sum_of_samples/num_samples)
    

print(monte_carlo(500000, 0, 5))