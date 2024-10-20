"""
estimate: 40 minutes
actual = 1 hours
"""


def main():
    user_data = {}
    used_emails = set()
    print("Enter an email")
    email = input("Email: ").strip().lower()
    while email != "":
        if email in used_emails:
            print("Email already exists in the database.")
        else:
            name = separate_name_from_email(email)
            confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
            if confirm == '' or confirm == 'y':
                user_data[email] = name
                used_emails.add(email)
            elif confirm == 'n':
                name = input("Name: ").strip()
                user_data[email] = name
                used_emails.add(email)
            else:
                print("Invalid input. Please enter Y or n.")

        email = input("Email: ").strip().lower()

    print("\nName and Email List:")
    for email, name in user_data.items():
        print(f"{name} ({email})")


def separate_name_from_email(email):
    """separate name from the email address."""
    username = email.split('@')[0]
    name_parts = username.split('.')
    capitalized_name = ' '.join(part.capitalize() for part in name_parts)
    return capitalized_name


main()
