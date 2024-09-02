from fuel import convert, gauge

def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("99/100") == 99

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"

if __name__ == "__main__":
    test_convert_valid()
    test_gauge()
    print("All tests passed!")
