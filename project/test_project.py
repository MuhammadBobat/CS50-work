import pytest
from project import check_app, validity

def main():
    test_check_app()
    test_validity()

def test_check_app():
    with pytest.raises(ValueError):
        assert check_app("***!")
    assert check_app("Twitter") == "T"
    assert check_app("twitter") == "T"

def test_validity():
    with pytest.raises(ValueError):
        assert validity("five")
    with pytest.raises(ValueError):
        assert validity("16")
    with pytest.raises(ValueError):
        assert validity("6")
    assert validity("8") == True

if __name__ == "__main__":
    main()