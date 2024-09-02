import pytest
from um import count

def test_single_um():
    assert count("um") == 1
def test_um_with_punctuation():
    assert count("um?") == 1
    assert count("um, thanks") == 1
def test_case_insensitivity():
    assert count("Um") == 1
    assert count("UM") == 1
def test_multiple_ums():
    assert count("Um, thanks, um...") == 2
    assert count("um um um") == 3
def test_no_um():
    assert count("yummy") == 0
    assert count("umbrella") == 0
def test_um_in_sentence():
    assert count("Um, thanks for the album.") == 1
    assert count("Do you like um, music?") == 1

if __name__ == "__main__":
    pytest.main()
