
usernames = [
    'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
    'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
    'Command', 'ExecState', 'InteractiveConsole',
    'InterpreterInterface', 'StartServer', 'bob'
]


def collect_numbers():
    numbers = []
    for _ in range(5):
        number = input("Number: ")
        while not number.replace('.', '', 1).isdigit():
            print("Please enter a valid number.")
            number = input("Number: ")
        numbers.append(float(number))
    return numbers


def output_numbers_info(numbers):
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


def main():
    # Collect and process numbers
    numbers = collect_numbers()
    output_numbers_info(numbers)

    # Check username
    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()

