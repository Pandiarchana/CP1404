from prac_09.car import Car


class Taxi(Car):
    _price_per_km: float = 1.23

    def __init__(self, name: str, fuel: float):
        super().__init__(name, fuel)
        self._current_fare_distance: float = 0

    def __str__(self) -> str:
        """Return a string representation of the Taxi."""
        return f"{super().__str__()}, {self._current_fare_distance:.2f}km on current fare, ${self._price_per_km:.2f}/km"

    def get_fare(self) -> float:
        return self._price_per_km * self._current_fare_distance

    def start_fare(self) -> None:
        self._current_fare_distance = 0

    def drive(self, distance: float) -> float:
        if distance < 0:
            raise ValueError("Distance must be positive.")
        distance_driven: float = super().drive(distance)
        self._current_fare_distance += distance_driven
        return distance_driven

