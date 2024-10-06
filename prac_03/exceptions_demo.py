"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
     It's occur when user enter a value that cannot be converted to be integer because int() is not used.

2. When will a ZeroDivisionError occur?
     It's occur when users input zero divide by any other value.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
     Check denominator before dividing
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot be divide by zero")
    else:
        fraction = numerator / denominator
        print(fraction)
except ZeroDivisionError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
