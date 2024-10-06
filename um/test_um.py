import pytest
from um import count

def test_um():
    assert count("um") == 1

def test_punctuation():
    assert count("um?") == 1
    assert count("Um, thanks, um...") == 2

def test_words():
    assert count("Um, thanks for the album.") == 1
