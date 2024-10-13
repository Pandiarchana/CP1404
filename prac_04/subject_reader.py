"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    try:
        with open(FILENAME) as input_file:
             for line in input_file:
                 line = line.strip()
                 if line:
                    parts = line.split(',')
                    if len(parts) == 3:
                       parts[2] = int(parts[2])
                       data.append(parts)
                    else:
                        print(f"Invalid format:{line}")
    except FileNotFoundError:
        print(f"Error: The file {FILENAME} was not found.")
    return


main()