def main():
    print("Menu")
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            converted_celsius_fahrenheit()
        elif choice == "F":
            converted_fahrenheit_celsius()
        else:
            print("Invalid choice")
        print("Menu")
        choice = input(">>>").upper()
    print("Thank you.")


def converted_celsius_fahrenheit():
    celsius = float(input("Celsius:"))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"Result:{fahrenheit:.2f}F")


def converted_fahrenheit_celsius():
    fahrenheit = float(input("Fahrenheit:"))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result:{celsius:.2f}C")


main()
