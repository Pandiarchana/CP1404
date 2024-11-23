from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()} plus flag_fall of ${self.flagfall:.2f}"

    def get_fare(self):
        return super().get_fare() + self.flagfall

