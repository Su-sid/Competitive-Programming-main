#!/bin/python3

import math
import os
import random
import re
import sys

def weird_checker(number: int)->str:
    
    # initialize an empty string
    status=''
    
    # check if a number is even or odd
    if not (number % 2) == 0:
        status=print('Weird')
        
    # check if a number if even and in range
    elif (number)in range(2, 5) or number >20:
        status=print('Not Weird')
    else:
        status=print('Weird')
    
    return status

if __name__ == '__main__':
    n = int(input().strip())
    
    weird_checker(n)
    
