from basics.src.inverse import inverse
import pytest

def test_long_list():
    assert inverse(["a","b","c","d","e"]) == "edcba"

def test_four_elements_list():
    assert inverse(["a","b","c","d"]) == "cba"    


def test_error_when_integer():
    with pytest.raises(ValueError):
        inverse(87)    

def test_error_when_list():
    with pytest.raises(ValueError):
        inverse(["a","b","c","d"])      

def test_lower_cases():
    assert inverse("hello") == "olleh"

def test_lower_cases_fiour_elements():
    assert inverse("hell") == "lleh"       