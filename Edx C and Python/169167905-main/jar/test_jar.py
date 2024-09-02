import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(8)

    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(11)

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(4)

    with pytest.raises(ValueError):
        jar.withdraw(-1)

if __name__ == "__main__":
    pytest.main()
