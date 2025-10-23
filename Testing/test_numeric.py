#!/usr/bin/env 
import pytest
def isnumeric(number):
    if (number) is int or float:
        print('True')
    if number is not int or float:
        print('False')

def num_test():
    expected='True'
    observed = isnumeric(1.3)
    assert observed == expected, f'expected {expected}, got {observed}'