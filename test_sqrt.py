import math

def test_sqrt():
    num=9
    assert math.sqrt(num) == 3

def test_square():
    
    num = 7
    assert num*num == 49

def test_check():
    x = 100

    assert x >=90

def test_multiply():
    x = 10
    y = 3

    assert x*y==30

def test_fun():
    x = 6
    assert x + 7 == 13