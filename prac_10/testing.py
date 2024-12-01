import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)  # Fixed to use join to add spaces between repeated strings


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length  # Fixed condition to handle "equal to length"


def format_sentence(phrase):
    """
    Format the given phrase as a sentence, starting with a capital letter and ending with a full stop.
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('python is fun')
    'Python is fun.'
    """
    phrase = phrase.capitalize()  # Capitalize the first letter
    if not phrase.endswith('.'):  # Ensure it ends with a full stop
        phrase += '.'
    return phrase


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"  # Fixed test to pass after fixing repeat_string function

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Test if Car sets the fuel correctly using both default and passed values
    car_default_fuel = Car()
    assert car_default_fuel.fuel == 0, "Car default fuel is not set correctly"

    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set fuel correctly when passed"

    # Test is_long_word
    assert is_long_word("not") == False, "is_long_word failed"
    assert is_long_word("supercalifrag") == True, "is_long_word failed"
    assert is_long_word("Python", 6) == True, "is_long_word failed"

    # Test format_sentence
    assert format_sentence("hello") == "Hello.", "format_sentence failed"
    assert format_sentence("It is an ex parrot.") == "It is an ex parrot.", "format_sentence failed"
    assert format_sentence("python is fun") == "Python is fun.", "format_sentence failed"



run_tests()


doctest.testmod()
