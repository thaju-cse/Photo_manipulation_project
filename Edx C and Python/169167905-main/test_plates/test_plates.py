import plates

def test_plates():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("ECTO88") == True
    assert plates.is_valid("NRVOUS") == True
    assert plates.is_valid("CS05") == False
    assert plates.is_valid("50") == False
    assert plates.is_valid("CS50P2") == False
    assert plates.is_valid("PI3.14") == False
    assert plates.is_valid("H") == False
    assert plates.is_valid("OUTATIME") == False

if __name__ == "__main__":
    test_plates()
