import math
import pytest

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def test_square():
    num = 7
    assert 7*7 == 40

def test_equality():
    assert 10 == 11

@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100

@pytest.fixture
def input_value():
    input = 39
    return input

def test_divisible_by_3(input_value):
    assert input_value % 3 == 0

def test_divisible_by_6(input_value):
    assert input_value % 6 == 0

