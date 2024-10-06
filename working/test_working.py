from working import convert
import pytest

def test_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_error():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 14 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 14 PM")

def test_both():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"