from seasons import get_date
import pytest

def test_get_date():
    assert get_date("1998-07-03") == ['1998', '07', '03']
