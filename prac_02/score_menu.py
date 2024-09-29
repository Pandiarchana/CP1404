

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50


def main():
    score = ""
    print("Menu:")
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
          score = get_score()
        elif choice == "P":
          score = get_grade(score)
        elif choice == "S":
          stars = get_show_stars(score)
        else:
          print("Invalid choice")
        print("Menu:")
    choice = input(">>>").upper()
    print("Farewell")


def get_score():
    score = float(input("Enter score:"))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid Score")
        score = float(input("Enter score:"))
    return score


def get_grade(score):
    if score >= EXCELLENT_THRESHOLD:
        message = "Excellent"
    elif score >= PASS_THRESHOLD:
        message = "Passable"
    else:
        message = "Bad"
    return message


def get_show_stars(score):
    if score > MINIMUM_SCORE:
        print("*" * score)


main()


