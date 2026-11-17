
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.app import welcome, add_numbers


# Test 1: Welcome message
def test_welcome():
    assert welcome() == "Secure Repository Starter is running!"


# Test 2: Addition of positive numbers
def test_add_numbers():
    assert add_numbers(10, 20) == 30


# Test 3: Addition with zero
def test_add_zero():
    assert add_numbers(5, 0) == 5


# Test 4: Addition of negative numbers
def test_add_negative_numbers():
    assert add_numbers(-5, -5) == -10


# Test 5: Invalid input
def test_add_invalid_input():
    with pytest.raises(TypeError):
        add_numbers("hello", 10)
