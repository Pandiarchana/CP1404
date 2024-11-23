from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0
    user_choice = "N"

    print("Let's drive!")

    while user_choice != "Q":
        print_menu(total_bill)
        user_choice = input(">>> ").upper()

        if user_choice == "C":
            current_taxi = choose_taxi(taxis)
        elif user_choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                total_bill = drive_car(current_taxi, total_bill)
        elif user_choice != "Q":
            print("Invalid option")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")


def print_menu(total_bill):
    print(f"\nBill to date: ${total_bill:.2f}")
    print("Menu:")
    print("q)uit")
    print("c)hoose taxi")
    print("d)rive")


def drive_car(current_taxi, total_bill):
    try:
        drive_distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return total_bill

    current_taxi.drive(drive_distance)
    trip_cost = current_taxi.get_fare()
    total_bill += trip_cost
    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    return total_bill


def choose_taxi(taxis):
    print("Taxis available: ")
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")

    while True:
        try:
            choice = int(input("Choose taxi: "))
            if 0 <= choice < len(taxis):
                return taxis[choice]
            else:
                print("Invalid taxi choice")
        except ValueError:
            print("Invalid choice. Please enter a number.")


main()


