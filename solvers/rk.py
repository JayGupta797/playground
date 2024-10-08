#!/usr/bin/env python
# coding: utf-8

import numpy as np

def read_butcher_tableau(filename):
    """Reads the Butcher tableau from a file."""
    with open(filename, 'r') as fhand:
        data = [np.array(line.strip().split(', ')).astype(float) for line in fhand]
    return data

def f(x, y):
    """Defines the implicit function f(x, y) = x^2 + y."""
    return x**2 + y

def runge_kutta(x, y, ts, data):
    """Performs one time step of runge kutta integration scheme"""
    # Initialize the list for storing k values
    kn = [f(x, y)]
    
    # Iterate through the stages of the Runge-Kutta method
    for i, arr in enumerate(data[1:-1]):
        tmpx = x + ts * arr[0]
        tmpy = y + ts * np.dot(kn, arr[1:])
        kn.append(f(tmpx, tmpy))
    
    # Compute the final y value using the last row of the Butcher tableau
    return y + ts * np.dot(data[-1], kn)

if __name__ == "__main__":
    # Define initial values
    initial_x = 0      # Initial x
    initial_y = 1      # Initial y
    time_step = 0.1    # Time step
    
    # Read data from the Butcher tableau
    butcher_tableau = read_butcher_tableau("tableau.txt")
    
    # Perform Runge-Kutta integration
    result_y = runge_kutta(initial_x, initial_y, time_step, butcher_tableau)
    
    # Output the result
    print("Result after one time step:", result_y)
