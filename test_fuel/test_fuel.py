from fuel import convert, gauge
import pytest

def test_input():
    assert convert("1/2") == 50
    assert gauge(50) == "50%"
    assert convert("1/100") == 1
    assert gauge(1) == "E"
    assert convert("99/100") == 99
    assert gauge(99) == "F"

def test_errors():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("cat/dog")

