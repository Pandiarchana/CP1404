class ProgrammingLanguage:
    """Represent the programming languages information"""

    def __init__(self, name, typing, reflection, years):
        """Create languages from the values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.years = years

    def __str__(self):
        """Return string representation"""
        return f"{self.name}, {self.typing} Typing, Reflection {self.reflection} , Appears in {self.years}"

    def is_dynamic(self):
        """Determine the program is typed in dynamically"""
        return self.typing == "Dynamic"


def testing():
    """Simple testing"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True,1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    testing()

