from numb3rs import validate
import pytest

def test_validate():
    assert validate(r"127.0.0.1") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.512.512.512") == False
    assert validate(r"1.2.3.1000") == False
    assert validate(r"cat") == False
    assert validate(r"1") == False
    assert validate(r'255.255.255.255') == True
    assert validate(r'256.255.255.255') == False
    assert validate(r'255.256.255.255') == False
    assert validate(r'255.255.256.255') == False
    assert validate(r'255.255.255.256') == False