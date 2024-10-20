import csv
from fileinput import filename


def main():
    filename = "wimbledon.csv"
    champions = read_wimbledon_data(filename)
    champion_wins = count_wins(champions)
    countries = get_win_countries(filename)
    display_champions_and_wins(champion_wins)
    display_countries_of_champions(countries)


def read_wimbledon_data(filename):
    champions = []
    with open(filename, "r", encoding="utf-8-sig") as in_files:
        reader = csv.reader(in_files)
        next(reader)
        for row in reader:
            champions.append((row[2], row[1]))
    return champions


def count_wins(champions):
    champions_wins = {}
    for champion, country in champions:
        if champion in champions_wins:
            champions_wins[champion] += 1
        else:
            champions_wins[champion] = 1
    return champions_wins


def get_win_countries(filename):
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as in_files:
        reader = csv.reader(in_files)
        next(reader)
        for row in reader:
            countries.add(row[1])
    sorted_countries = sorted(countries)
    return sorted_countries


def display_champions_and_wins(champion_wins):
    print("Wimbledon champions")
    for champion, wins in sorted(champion_wins.items()):
        print(f"{champion} {wins}")


def display_countries_of_champions(countries):
    print("These", len(countries), "countries have won Wimbledon:")
    countries_string = ",".join(countries)
    print(countries_string)


main()

