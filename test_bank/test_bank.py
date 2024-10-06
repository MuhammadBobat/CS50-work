from bank import value

def test_withH():
    assert value("Hi") == 20
    assert value("hey man") == 20

def test_with_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HeLlO") == 0

def test_withoutH():
    assert value("What's up") == 100
