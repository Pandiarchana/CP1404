"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def get_odometer(self):
        """Return the odometer reading."""
        return self._odometer

    def get_fuel(self):
        """Return the current fuel level."""
        return self.fuel


if __name__ == "__main__":
    my_car = Car(10)
    print(f"Initial fuel: {my_car.get_fuel()}")

    driven_distance = my_car.drive(5)
    print(f"Drove: {driven_distance} km")
    print(f"Remaining fuel: {my_car.get_fuel()}")
    print(f"Odometer reading: {my_car.get_odometer()} km")

    driven_distance = my_car.drive(10)
    print(f"Drove: {driven_distance} km")
    print(f"Remaining fuel: {my_car.get_fuel()}")
    print(f"Odometer reading: {my_car.get_odometer()} km")