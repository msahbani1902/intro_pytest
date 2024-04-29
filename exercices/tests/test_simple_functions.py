from exercices.src.simple_functions import add, divide, add_integer,alea_uniform
import pytest

def test_add():
    assert add(3,5) == 8


def test_divide():
    assert int(divide(4,2)) == 2 

def test_add_integer():
    assert add_integer(3,4) ==7


def test_fail_add_integer():
    with pytest.raises(TypeError):
        add_integer(4,"a") 

def test_alea_uniform():
    assert alea_uniform(3,4) > 3 and alea_uniform(3,4) < 4
    assert alea_uniform(4,3) > 3 and alea_uniform(4,3) < 4