"""
word occurences
estimate: 45 minutes
actual = 1.30 hours
"""


def main():
    string = input("Enter a string: ")
    counts = count_word_occurrences(string)
    print("Word counts:")
    print_word_counts(counts)


def count_word_occurrences(string):
    """count the word and return word_count"""
    word_counts = {}
    words = string.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def print_word_counts(word_counts):
    """Find the length of the longest word for formatting and sort word alphabetically """
    max_length = max(len(word) for word in word_counts.keys())
    sorted_words = sorted(word_counts.keys())
    for word in sorted_words:
        print(f"{word:>{max_length}} : {word_counts[word]}")


main()

