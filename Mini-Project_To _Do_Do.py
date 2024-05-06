# Module 2: Mini-project | To-Do list Application
# Introduction


# In this project, you will apply your Python programming skills to create a functional To-Do List Application from scratch. 
# The objective of this project is to reinforce your understanding of Python syntax, data types, control structures, functions, 
# and error handling while building a practical and interactive application.

# Project Requirements


# User Interface (UI):
# Create a command-line interface (CLI) for the To-Do List Application.
# Display a welcoming message and a menu with the following options:
# ```
# Welcome to the To-Do List App!
#     Menu:
#     1. Add a task
#     2. View tasks
#     3. Mark a task as complete
#     4. Delete a task
#     5. Quit

#     ```
# To-Do List Features:
#   Implement the following features for the To-Do List:
#   - Adding a task
#   - Viewing the list of tasks with from Incomplete and Complete tasks.
#   - Marking a task as complete.
#   - Deleting a task.
#   - Quitting the application.

# User Interaction:
#   - Allow users to interact with the application by selecting menu options using input().
#   - Implement input validation to handle unexpected user input gracefully.

# Error Handling:
#   - Implement error handling using try, except, else, and finally blocks to handle potential issues.

# Code Organization:
#   - Organize your code into functions to promote modularity and readability.
#   - Use meaningful function names with appropriate comments and docstrings for clarity.

# Testing and Debugging:
#   - Thoroughly test your application to identify and fix any bugs.
#   - Consider edge cases, such as empty task lists or incorrect user input.

# Documentation:
#   - Include a README file that explains how to run the application and provides a brief overview of its features.

# Optional Features (Bonus):
#   - If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.

# GitHub Repository:
#   - Create a GitHub repository for your project.
#   - Commit your code to the repository regularly.
#   - Include a link to your GitHub repository in your project documentation. -->


# We are starting off by creating two lists that are used to store tasks that are incomplete and completed, respectively.

incomplete_tasks = []
completed_tasks = []

# The add_task() function allows the user to add a task to the list of tasks. It prompts the user to enter a task, checks if the task 
# is already in the list, and adds it if not. It then prints a message indicating whether the task was added successfully.

def add_task(tasks):
    task = input("\nWhat would you like to add to your tasks? ").lower()
    if task not in tasks:
        tasks.append(task)
        print(f'{task} is added to your tasks. Here is the list of tasks:')
    else:
        print(f"{task} is already in your tasks:")

# The view_tasks() function displays all the tasks in the list of tasks. If the list is empty, it prints "None" to indicate 
# there are no tasks.

def view_tasks(tasks):
    print("Here are your tasks:")
    for task in tasks:
        print(task)
    if not tasks:
        print(None)

# The 'mark_complete()' function allows the user to mark a task as complete. It prompts the user to enter the task they want to mark, 
# removes it from the 'incomplete_tasks' list (specified by the 'tasks' parameter), adds it to the 'completed_asks' list (specified 
# byt the 'accomplishments' parameter), and prints a message confirming completion. While we can access 'incomplete_tasks' and 
# 'completed_tasks' within the function because they are global variables, we should not do so because it is considered bad practice 
# and leads to messy code.

def mark_complete(tasks, accomplishments):
    task = input("\nWhich task would you like to mark as complete? ").lower()
    try:
        tasks.remove(task)
        accomplishments.append(task)
        print(f"{task} is marked as complete!")
        print(accomplishments)
    except ValueError:
        print(f'{task} is not in your tasks yet!')

# The view_all_tasks() function displays all the accomplishments (completed_tasks) and gives the user the option to view their 
# current tasks (incomplete_tasks). If the user chooses to view tasks, it calls the view_tasks function. If not, it goes back
# to the menu (initial options). If the user gives a wrong answer, it keeps asking for a valid response (yes or no).

def view_all_tasks(tasks, accomplishments):
    print("Here are your accomplishments:")
    for task in accomplishments:
        print(task)
    if not accomplishments:
        print(None)
    while True:
        response = input("\nWould you like to see your current tasks? Yes/No: ").lower()
        if response == "yes":
            view_tasks(tasks)
            break
        elif response != "no":
            print("Please enter a valid response!")
            continue
        else:
            break

# The delete_task function allows the user to delete a task from the list of incomplete tasks. It prompts the user to enter the task 
# they want to delete, removes it from the list if it exists, and prints a message confirming the deletion.

def delete_task(tasks):
    task = input("\nWhich task would you like to remove? ").lower()
    try:
        tasks.remove(task)
        print(f"{task} is no longer in your tasks! Here is what is left in your list:")
    except ValueError:
        print(f'{task} is not in your tasks yet!')

# to_do_list() is the main function that implements the To-Do List App. It presents a menu of options to the user and executes 
# the corresponding functions based on the user's choice. The loop continues until the user chooses to quit.

def to_do_list(tasks, accomplishments):
    while True:
        print("\nWelcome to the To-Do List App!")
        print("\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. View accomplishments")
        print("5. Delete a task")
        print("6. Quit")

        choice = input("\nWhat would you like to do? Enter your choice from 1 to 5: ")
        if choice == "1":
            add_task(tasks)
            print(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks, accomplishments)
        elif choice == "4":
            view_all_tasks(tasks, accomplishments)
        elif choice == "5":
            delete_task(tasks)
            print(tasks)
        elif choice == "6":
            print("\nYour tasks are:")
            for task in tasks:
                print(task)
            if not tasks:
                print(None)
            print("\nYour accomplishments are:")
            for accomplishment in accomplishments:
                print(accomplishment)
            if not accomplishments:
                print(None)
            break
        else:
            print("Please enter a valid response!")

to_do_list(incomplete_tasks, completed_tasks)