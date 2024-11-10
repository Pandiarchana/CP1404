import datetime


class Project:
    """Represents a project with attributes for name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project object with provided attributes."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def display(self):
        """return the formatted string"""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def update_completion(self, new_completion):
        """
        Update the completion percentage of the project"""
        self.completion_percentage = new_completion

    def update_priority(self, new_priority):
        """Update the priority level of the project."""
        self.priority = new_priority

    def start_after_date(self, compare_date):
        """Check if the project starts after a given date"""
        return self.start_date > compare_date

    def __lt__(self, other):
        """determine if this project has lower priority than another."""
        return self.priority < other.priority

    def __repr__(self):
        """Return a string representation of the Project"""
        return self.display()
