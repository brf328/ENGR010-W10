import my_module as mod
import pytest

def test_plot():
    x = [x for x in range(10)]
    assert mod.plot("cos", x) == 3

def test_Chooser():
    num = 3
    assert mod.Chooser() == num

def test_Die():
    num = 4
    assert mod.Die() == num