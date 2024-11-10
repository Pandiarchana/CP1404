class Guitar:
    """represent a Guitar object"""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """return information of the guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """calculate the age of the guitar"""
        return current_year - self.year

    def is_vintage(self, current_year):
        """check if the guitar is vintage"""
        return self.get_age(current_year) >= 50
