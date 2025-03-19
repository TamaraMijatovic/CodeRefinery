import pytest

def fizz_buzz(a):
    if a==0:
        raise ValueError
    return

def test_fizz_buzz_zero_or_negative():
    with pytest.raises(ValueError):
        fizz_buzz(0)
    with pytest.raises(ValueError):   
        fizz_buzz(1)

def test_fizz_buzz_multiple_of_3():
    assert(fizz_buzz(3)=="Fizz")
    assert(fizz_buzz(6)=="Fizz")

def test_fizz_buzz_multiple_of_5():
    assert(fizz_buzz(5)=="Buzz")
    assert(fizz_buzz(10)=="Buzz")

def test_fizz_buzz_multiple_of_3_and_5():
    assert(fizz_buzz(15)=="FizzBuzz")
    assert(fizz_buzz(30)=="FizzBuzz")
    
