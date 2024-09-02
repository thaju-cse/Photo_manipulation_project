from bank import value

def test_bank():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("HEY") == 20
    assert value("h") == 20
    assert value("what's up") == 100
    assert value("good morning") == 100
    assert value("Goodbye") == 100
    assert value("") == 100

if __name__ == "__main__":
    test_bank()
