"""
CP1404/CP5632 Practical
Car class
"""
from prac_09.car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name: str, fuel: float, price_per_km: float):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.__price_per_km = max(0, price_per_km)
        self.__current_fare_distance = 0

    def __str__(self) -> str:
        """Return a string representation of Taxi."""
        return f"{super().__str__()}, {self.__current_fare_distance}km on current fare, ${self.__price_per_km:.2f}/km"

    def get_fare(self) -> float:
        """Return the price for the taxi trip."""
        return self.__price_per_km * self.__current_fare_distance

    def start_fare(self) -> None:
        self.__current_fare_distance = 0

    def drive(self, distance: float) -> float:
        distance_driven = super().drive(distance)
        self.__current_fare_distance += max(0, distance_driven)
        return distance_driven

