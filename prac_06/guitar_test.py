
from guitar import Guitar


def test_guitar_methods():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 500.00)

    current_year = 2022
    age1 = guitar1.get_age(current_year)
    age2 = guitar2.get_age(current_year)

    print(f"Gibson L-5 CES get_age() - Expected 100. Got {age1}")
    print(f"Another Guitar get_age() - Expected 9. Got {age2}")

    vintage1 = guitar1.is_vintage(current_year)
    vintage2 = guitar2.is_vintage(current_year)

    print(f"Gibson L-5 CES is_vintage() - Expected True. Got {vintage1}")
    print(f"Another Guitar is_vintage() - Expected False. Got {vintage2}")



test_guitar_methods()

