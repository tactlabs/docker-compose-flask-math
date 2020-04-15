import pytest

import math_util

def test_math_add_1():
    
    a = 1
    b = 2

    assert math_util.add(a, b) == 3

def test_math_add_2():
    
    a = 11
    b = 20

    assert math_util.add(a, b) == 31

def test_math_add_3():
    
    a = 6
    b = 19

    assert math_util.add(a, b) == 25

def test_math_subtract_1():
    
    a = 10
    b = 2

    assert math_util.subtract(a, b) == 8

def test_math_subtract_2():
    
    a = 40
    b = 14

    assert math_util.subtract(a, b) == 26

def test_math_subtract_3():
    
    a = 45
    b = 1

    assert math_util.subtract(a, b) == 44
