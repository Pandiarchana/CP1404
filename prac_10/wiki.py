import wikipedia


def get_wikipedia_page():
    while True:
        # Prompt the user for a page title or search phrase
        title = input("Enter page title: ")

        # Exit condition for the loop
        if not title:
            print("Thank you.")
            break

        try:
            # Attempt to retrieve the page based on the title
            page = wikipedia.page(title, autosuggest=False)
            print(f"\n{page.title}")
            print(f"{page.summary}\n{page.url}")

        except wikipedia.exceptions.DisambiguationError as e:
            # If there's a disambiguation error, list possible suggestions
            print(f"\nWe need a more specific title. Try one of the following, or a new search:\n{e.options}")

        except wikipedia.exceptions.PageError:
            # If the page doesn't exist, notify the user
            print(f"\nPage id \"{title}\" does not match any pages. Try another id!\n")

        except Exception as e:
            # Handle any other unexpected exceptions
            print(f"An error occurred: {e}\n")


if __name__ == "__main__":
    get_wikipedia_page()
