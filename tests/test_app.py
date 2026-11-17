
from src.app import welcome, add_numbers


def test_welcome():
    assert welcome() == "Secure Repository Starter is running!"


def test_add_numbers():
    assert add_numbers(10, 20) == 30


def test_add_zero():
    assert add_numbers(5, 0) == 5

