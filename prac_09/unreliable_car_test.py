from prac_09.unreliable_car import UnreliableCar


def main():
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        distance_driven_good = good_car.drive(i)
        distance_driven_bad = bad_car.drive(i)

        if distance_driven_good:
            print(f"{good_car.name:12} drove {distance_driven_good}km")
        else:
            print(f"{good_car.name:12} failed to drive {i}km")

        if distance_driven_bad:
            print(f"{bad_car.name:12} drove {distance_driven_bad}km")
        else:
            print(f"{bad_car.name:12} failed to drive {i}km")

    print("\nFinal odometer readings:")
    print(good_car)
    print(bad_car)


main()

