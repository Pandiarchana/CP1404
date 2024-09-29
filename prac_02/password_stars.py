PASSWORD_LENGTH = 10


def main():
    password = validate_password
    print(len("password") * "*")


def validate_password():
    password = input("Enter password:")
    while len(password) < PASSWORD_LENGTH:
        print("Invalid Password")
        password = input("Enter password:")
    return password


main()

