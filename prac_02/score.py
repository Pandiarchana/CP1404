import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50


def main():
    score = get_score()
    grade = get_grade(score)
    print("garde")
    random_number = random.uniform(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(random_number)
    random_garde = get_grade(random_number)
    print(random_garde)


def get_grade(score):
    if score >= EXCELLENT_THRESHOLD:
        message = "Excellent"
    elif score >= PASS_THRESHOLD:
        message = "Passable"
    else:
        message = "Bad"
    return message


def get_score():
    score = float(input("Enter score:"))
    while score < MINIMUM_SCORE or score > MINIMUM_SCORE:
        print("Invalid Score")
        score = float(input("Enter score:"))
    return score


main()


