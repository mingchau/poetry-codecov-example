from math_operations.calculator import add, multiply

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(-3, 2) == -6