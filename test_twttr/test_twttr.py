from twttr import shorten

def test_cases():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("HeLlO") == "HLl"

def test_numbers():
    assert shorten("123") == "123"

def test_spag():
    assert shorten(",.!?") == ",.!?"



if __name__ == "__main__":
    main()
