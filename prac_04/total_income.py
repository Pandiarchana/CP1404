"""
CP1404/CP5632 Practical - Suggested Solution
Cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)


def get_incomes(number_of_months):
    """Collect income data for all  months."""
    incomes = []
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter monthly income {month}: "))

        # Simple validation for income
        while income < 0:
            print("Please enter a valid income.")
            income = float(input(f"Enter monthly income {month}: "))

        incomes.append(income)
    return incomes


def print_report(incomes):
    """Print report based on incomes."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()