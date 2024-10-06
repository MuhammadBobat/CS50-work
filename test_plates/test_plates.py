from plates import is_valid

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("H") == False
    assert is_valid("PLATES22") == False


def test_beginning():
    assert is_valid("RLCS") == True
    assert is_valid("W2X4") == False
    assert is_valid("224") == False


def test_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_firstnumber():
    assert is_valid("CS05") == False

def test_spag():
    assert is_valid("CS50!") == False