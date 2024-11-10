"""
start date = 2024 November 05
start time = 9.30PM

"""

import datetime
from operator import itemgetter

FILENAME = "projects.txt"
menu = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print("Welcome to Pythonic Project Management")
    choice = ''
    while choice != 'q':
        print(menu)
        choice = input(">>> ").strip().lower()
        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            save_choice = input(f"Would you like to save to {FILENAME}? ").strip().lower()
            if save_choice.startswith('y'):
                save_projects(projects, FILENAME)
                print(f"Projects saved to {FILENAME}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date = input("Show projects that start after date (dd/mm/yyyy): ")
            sorted_projects = filter_projects_by_date(projects, date)
            display_projects(sorted_projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input(f"Would you like to save to {FILENAME}? ").strip().lower()
            if save_choice.startswith('y'):
                save_projects(projects, FILENAME)
                print(f"Projects saved to {FILENAME}")
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid choice. Please try again.")


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    try:
        with open(filename, 'r') as infile:
            next(infile)  # Skip header if any
            for line in infile:
                if line.strip():
                    parts = line.strip().split('|')
                    # Assuming your file has: name | start_date | priority | cost_estimate | completion_percentage
                    name, start_date, priority, cost_estimate, completion_percentage = parts
                    project = {
                        'name': name.strip(),
                        'start_date': datetime.datetime.strptime(start_date.strip(), '%d/%m/%Y').date(),
                        'priority': int(priority.strip()),
                        'cost_estimate': float(cost_estimate.strip()),
                        'completion_percentage': int(completion_percentage.strip())
                    }
                    projects.append(project)
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    return projects


def save_projects(projects, filename):
    """Save projects to a file."""
    with open(filename, 'w') as outfile:
        outfile.write("Name | Start Date | Priority | Cost Estimate | Completion Percentage\n")
        for project in projects:
            outfile.write(f"{project['name']} | {project['start_date'].strftime('%d/%m/%Y')} | "
                          f"{project['priority']} | {project['cost_estimate']:.2f} | {project['completion_percentage']}\n")


def add_new_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate ($): ")
    completion_percentage = input("Percent complete: ")

    new_project = {
        'name': name.strip(),
        'start_date': datetime.datetime.strptime(start_date.strip(), '%d/%m/%Y').date(),
        'priority': int(priority.strip()),
        'cost_estimate': float(cost_estimate.strip()),
        'completion_percentage': int(completion_percentage.strip())
    }
    projects.append(new_project)


def update_project(projects):
    """Update completion percentage and priority of a project."""
    for index, project in enumerate(projects):
        print(f"{index} {project['name']}")
    if not projects:
        print("No projects to update.")
        return
    try:
        index = int(input("Project choice: "))
        if 0 <= index < len(projects):
            new_completion = input("New Percentage: ")
            new_priority = input("New Priority: ")
            if new_completion:
                projects[index]['completion_percentage'] = int(new_completion)
            if new_priority:
                projects[index]['priority'] = int(new_priority)
            print("Project updated successfully.")
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


def display_projects(projects):
    """Display formatted data of projects."""
    incomplete_count = 0
    total_cost_estimate = 0.0
    number = 0
    formatted_projects = []

    # Adjust for better formatting
    max_name_length = max(len(project['name'].strip()) for project in projects)
    max_start_date_length = max(len(project['start_date'].strftime('%d/%m/%Y')) for project in projects)
    max_priority_length = max(len(str(project['priority'])) for project in projects)
    max_cost_estimate_length = max(len(f"${project['cost_estimate']:.2f}") for project in projects)
    max_completion_length = max(len(str(project['completion_percentage'])) for project in projects)

    projects.sort(key=lambda p: (p['priority'], p['name']))  # Sorting by priority and name
    for project in projects:
        number += 1
        if project['completion_percentage'] < 100:
            incomplete_count += 1
            total_cost_estimate += project['cost_estimate']
            formatted_projects.append(
                f"*{number}. {project['name']:<{max_name_length}} | {project['start_date'].strftime('%d/%m/%Y'):<{max_start_date_length}} | "
                f"{project['priority']:<{max_priority_length}} | ${project['cost_estimate']:.2f} | {project['completion_percentage']}%"
            )
        else:
            formatted_projects.append(
                f" {number}. {project['name']:<{max_name_length}} | {project['start_date'].strftime('%d/%m/%Y'):<{max_start_date_length}} | "
                f"{project['priority']:<{max_priority_length}} | ${project['cost_estimate']:.2f} | {project['completion_percentage']}%"
            )
    for project in formatted_projects:
        print(project)
    print_project_status(incomplete_count, total_cost_estimate)


def print_project_status(incomplete_count, total_cost_estimate):
    """Print message based on number of incomplete projects and total cost estimate."""
    if incomplete_count > 0:
        print(
            f"There are {incomplete_count} incomplete projects with a total cost estimate of ${total_cost_estimate:.2f}.")
    else:
        print("All projects are completed. Great job!")


def filter_projects_by_date(projects, date):
    """Filter projects that start after the given date."""
    try:
        filter_date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project['start_date'] > filter_date]
        return filtered_projects
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return []


if __name__ == "__main__":
    main()
