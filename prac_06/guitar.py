class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        return current_year - self.year

    def is_vintage(self, current_year):
        return self.get_age(current_year) >= 50


if __name__ == "__main__":
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(my_guitar)  # Output: Gibson L-5 CES (1922) : $16,035.40
    current_year = 2022
    print(f"Age: {my_guitar.get_age(current_year)} years")  # Output: Age: 100 years
    print(f"Is vintage? {'Yes' if my_guitar.is_vintage(current_year) else 'No'}")  # Output: Is vintage? Yes

