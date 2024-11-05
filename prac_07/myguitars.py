import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = load_guitars(FILENAME)
    show_guitars = display_guitars(guitars)
    print("My Guitars!")
    add_guitar(guitars)
    guitars.sort()
    print("\nSorted List of Guitars:")
    display_guitars(guitars)
    save_guitars(FILENAME, guitars)
    print(f"\nGuitars saved to {FILENAME}")


def load_guitars(FILENAME):
    guitars = []

    with open(FILENAME, 'r') as infile:
        reader = csv.reader(infile)
        for line in reader:
            if len(line) == 3:
                    name, year, cost = line
                    year = int(year)
                    cost = float(cost)
                    guitars.append(Guitar(name, year, cost))
    return guitars


def add_guitar(guitars):
    print("Enter details of the guitar: ")
    name = input("Name: ").strip()
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        name = input("Name: ").strip()


def display_guitars(guitars):
    if guitars:
        max_name_length = max(len(guitar.name) for guitar in guitars)
        max_cost_length = max(len(f"${guitar.cost:,.2f}") for guitar in guitars)
        for guitar in guitars:
            print(f"{guitar.name.ljust(max_name_length)} ({guitar.year}) : ${guitar.cost:,.2f}")
    else:
        print("No guitars entered.")


def save_guitars(FILENAME, guitars):
    with open(FILENAME, 'w') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


main()