from datetime import date
from seasons import calculate_minutes, minutes_to_words

def test_calculate_minutes():
    assert calculate_minutes(date(2023, 6, 17)) == (date(2024, 6, 17) - date(2023, 6, 17)).days * 1440
    assert calculate_minutes(date(2000, 1, 1)) == (date(2024, 6, 17) - date(2000, 1, 1)).days * 1440

def test_minutes_to_words():
    assert minutes_to_words(527040) == "five hundred twenty-seven thousand forty"
    assert minutes_to_words(1052640) == "one million fifty-two thousand six hundred forty"

if __name__ == "__main__":
    import pytest
    pytest.main()
