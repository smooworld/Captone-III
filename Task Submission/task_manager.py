# Imported datetime to get todays date
from datetime import date
import os.path

"""Defined a function that requests input from user to enter the date in
DD/MM/YYYY format and changes the input format of the date to the
same input in textfile and return date in new format"""


def date_due():
    month_dict = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May",
                  6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct",
                  11: "Nov", 12: "Dec"}

    due_month = 13
    due_date = input("Enter the due date for the task? (DD/MM/YYYY) \n")
    if due_date[3:5]:
        due_month = int(due_date[3:5])
    while len(due_date) != 10 or due_month > 12:
        due_date = input("Date entered in wrong format:"
                         "Please enter date again:(DD/MM/YYYY) \n")
        if due_date[3:5]:
            due_month = int(due_date[3:5])
    else:
        due_date = due_date.replace(" ", "/").split("/")
    due_month = month_dict[int(due_date[1])]
    due_date = f"{due_date[0]} {due_month} {due_date[2]}"
    return due_date


"""Defined a function to see if user is admin and Request user
to provide username and password and confirm password for
a new user.
once all information is received from user write data to a
file "user.txt"
Print message to console telling user that the new user has
been registered """


def reg_user(username):
    users = []
    with open("user.txt", "r", encoding="utf-8-sig") as user_file:
        for line in user_file:
            split_line = line.split(", ")
            users.append(split_line[0])
    if username == "admin":
        print("=" * 30)
        new_username = input("Enter a username: \n")
        print("=" * 30)
        while len(new_username) == 0 or new_username in users:
            if len(new_username) == 0:
                new_username = input("Enter a username: \n")
                print("=" * 30)
            elif new_username in users:
                new_username = input("Username already taken"
                                     " please enter another one:\n")
                print("=" * 30)
        new_password = input("Enter a password: \n")
        print("=" * 30)
        confirm_pw = input("Please confirm password: \n")
        print("=" * 30)
        while new_password != confirm_pw:
            confirm_pw = input("Confirmation password is incorrect! \n"
                               "Please confirm your password: \n")
            print("=" * 30)

        # Learned how to open file in append mode to not overwrite current
        # data in file
        with open("user.txt", "a", encoding="utf-8-sig") as users_file:
            users_file.write(f"{new_username}, {new_password}\n")

        print("=" * 30)
        print("User Registered.")
        print("=" * 30)


"""Defined a function to request input from user to provide the following:
Task, user for whom the task is for, description of task,
due date for task, and if task is completed or not.
The assigned date is today's date obtained by using
date.today() and using strftime to have it in the 
correct format.
After all data is received read data to a text file
Print message to console informing user that the
task was saved"""


def add_task():
    user = input("Enter a user to assign a task to: \n")
    print("=" * 30)
    task_title = input("Enter the title for your task: \n")
    print("=" * 30)
    task = input("Enter task description: \n")
    print("=" * 30)
    date_assigned = (date.today()).strftime("%d %b 20%y")
    due_date = date_due()
    print("=" * 30)
    is_complete = input("Is the task completed? Yes/No \n").capitalize()
    print("=" * 30)
    with open("tasks.txt", "a", encoding="utf-8-sig") as task_file:
        task_file.write(f"{user}, {task_title}, {task}, {date_assigned}"
                        f", {due_date}, {is_complete}\n")

    print("Task stored.")
    print("=" * 30)


"""Defined a function that will read all the lines in the
'tasks.txt' file using a for loop and print the
data to console in a neat readable manner. """


def view_all():
    content = []
    total_tasks = 0
    print("=" * 30)
    print("Viewing all tasks:")
    with open("tasks.txt", "r", encoding="utf-8-sig") as task_file:
        for line in task_file:
            total_tasks += 1
            content = line.split(", ")
            task_complete = content[5].replace("\n", "")
            print("=" * 30)
            print(f"Task {total_tasks}\n\n"
                  f"Task:            \t{content[1]} \n"
                  f"Assigned to:     \t{content[0]} \n"
                  f"Date Assigned:   \t{content[3]} \n"
                  f"Due Date:        \t{content[4]} \n"
                  f"Task Complete?   \t{task_complete} \n"
                  f"Task Description: \n{content[2]}")
        print("=" * 30)
    print(f"Total tasks: {total_tasks}")
    print("=" * 30)


"""Defined a function where the first part of the function
reads all the lines in the 'tasks.txt' file
using a for loop if the user in the line is the
same as the logged in user print the task to console in a neat and
readable manner."""


def view_mine(username):
    content = []
    all_tasks = []
    all_user_tasks = []
    total_tasks = 0
    print("=" * 30)
    print(f"Viewing all tasks for {username}")
    with open("tasks.txt", "r", encoding="utf-8-sig") as task_file:
        print("=" * 30)
        for i, line in enumerate(task_file):
            all_tasks.append(line)
            content = line.split(", ")
            task_complete = content[5].replace("\n", "")
            if content[0].lower() == username.lower():
                all_user_tasks.append(line)
                total_tasks += 1
                print(f"Task {total_tasks}\n\n"
                      f"Task:            \t{content[1]} \n"
                      f"Assigned to:     \t{content[0]} \n"
                      f"Date Assigned:   \t{content[3]} \n"
                      f"Due Date:        \t{content[4]} \n"
                      f"Task Complete?   \t{task_complete} \n"
                      f"Task Description: \n{content[2]}")
                print("=" * 30)
    print(f"You have {total_tasks} task/s.")
    print("=" * 30)

    """Second part of function requests user to choose a task to edit by 
    typing the corresponding number on the task.
    Request input from user to select a option of what to to with task
    Task can either be marked as done of edited.
    If chosen to edit user can change due_date and username the
    task was assigned to.   
    Write "tasks.txt" file with edited lines"""
    task_choice = int(input("Enter the number of the task you would"
                            " like to edit:\n(Enter -1 to"
                            " go back to the main menu)\n>"))

    while task_choice > total_tasks:
        task_choice = int(input("Task not found choose again:"))

    if task_choice == -1:
        pass
    else:
        task = all_user_tasks[task_choice - 1]
        task = task.split(", ")
        print("=" * 30)
        task_option = int(input("What would you like to do with this "
                                "task?\n(Enter the corresponding number)\n"
                                "\n---------------------------"
                                "\n|1 - Mark task as complete|\n"
                                "|2 - Edit task            |\n"
                                "|0 - Return to main menu  |\n"
                                "---------------------------\n\n>"))
        task_done = task[5].replace("\n", "")
        if task_option == 1 and task_done == "No":
            task[5] = "Yes\n"
            print("=" * 30)
            print("Marking task as Done!")
            print("=" * 30)
        elif task_option == 2 and task_done == "No":
            while True:
                print("=" * 30)
                edit_choice = input("What would you like to edit:"
                                    "(Enter the corresponding number)\n\n"
                                    "--------------------------------\n"
                                    "|1 - Username                  |\n"
                                    "|2 - Due date                  |\n"
                                    "|0 - Save and back to main menu|\n"
                                    "--------------------------------\n>")
                print("=" * 30)
                if edit_choice == "1":
                    print("=" * 30)
                    task[0] = input("Enter a new username: \n>")
                elif edit_choice == "2":
                    task[4] = date_due()
                elif edit_choice == "0":
                    print("=" * 30)
                    print("SAVING FILE... \nBack to main menu!")
                    print("=" * 30)
                    break
        elif task_done == "Yes" and task_option != 0:
            print("=" * 30)
            print("Task is already complete")
            print(task_option)
            print("=" * 30)

        elif task_option == 0:
            print("=" * 30)
            print("Back to main menu!")
            print("=" * 30)

        for i, task_data in enumerate(all_tasks):
            if task_data == all_user_tasks[task_choice - 1]:
                new_task = ", ".join(task)
                all_tasks[i] = new_task

        with open("tasks.txt", "w", encoding="utf-8-sig") as task_file:
            for line in all_tasks:
                task_file.write(line)


def gen_reports():
    """Generate reports for tasks by looping through the "task.txt" files
    data. Determine by loping through the data in each line if the task
    is complete, incomplete or overdue.
    Also determine how many tasks each user has, needs to complete
    or is overdue and read data to a dictionary.
    Calculate what percentage is incomplete and overdue of the total
    tasks and individual tasks for users.
    write all determined and calculated data to 'task_overview.txt'
    and 'user_overview.txt' """

    total_tasks = 0
    incompleted_tasks = 0
    overdue_tasks = 0
    data = []
    user_data = []
    users = {}
    total_users = 0
    user_tasks = 0
    user_incomplete = 0
    user_overdue = 0

    with open("user.txt", "r", encoding="utf-8-sig") as user_file:
        for line in user_file:
            total_users += 1
            user_data = line.split(", ")
            if user_data[0] not in users:
                users[user_data[0]] = [0, 0, 0]

    with open("tasks.txt", "r", encoding="utf-8-sig") as task_file:
        for line in task_file:
            data = line.split(", ")
            if data[0] in users:
                users[data[0]][0] += 1
                if data[5] == "No\n":
                    users[data[0]][1] += 1
                if data[4] < (date.today()).strftime("%d %b 20%y"):
                    users[data[0]][2] += 1
            else:
                user_tasks = 1
                if data[5] == "No\n":
                    user_incomplete += 1
                    if data[4] < (date.today()).strftime("%d %b 20%y"):
                        user_overdue += 1
                users[data[0]] = [user_tasks, user_incomplete, user_overdue]
            total_tasks += 1
            if data[5] == "No\n":
                incompleted_tasks += 1
                if data[4] < (date.today()).strftime("%d %b 20%y"):
                    overdue_tasks += 1

    completed_tasks = total_tasks - incompleted_tasks
    incomplete_percent = round((incompleted_tasks / total_tasks) * 100, 2)
    overdue_percent = round((overdue_tasks / total_tasks) * 100, 2)
    line = ", ".join([str(total_tasks), str(completed_tasks),
                      str(incompleted_tasks), str(overdue_tasks),
                      str(incomplete_percent), str(overdue_percent)])

    with open("task_overview.txt", "w", encoding="utf-8-sig") as task_overview_file:
        task_overview_file.write(line)

    for user in users:
        user_task_percentage = round((users[user][0] / total_tasks) * 100, 2)
        if users[user][0] != 0:
            task_percentage_incomp = round((users[user][1] / users[user][0]) * 100
                                           , 2)
        task_percentage_comp = 100 - task_percentage_incomp
        user_overdue_percentage = round((users[user][2] / total_tasks) * 100, 2)
        users[user] += [user_task_percentage, task_percentage_comp,
                        task_percentage_incomp, user_overdue_percentage]

    with open("user_overview.txt", "w", encoding="utf-8-sig") as user_overview_file:
        new_line = ""
        report_date = (date.today()).strftime("%d %b 20%y")
        user_overview_file.write(f"Report Date: {report_date}\n")
        user_overview_file.write(f"Total users: {len(users)}\n")
        user_overview_file.write(f"Total tasks: {total_tasks}\n")
        for user, data in users.items():
            new_line = "".join(str(data))
            new_line = user + new_line.replace("[", ", ")
            new_line = new_line.strip("]")
            user_overview_file.write(new_line + "\n")

    print("=" * 30)
    print("Reports Generated!")
    print("=" * 30)


"""Read the data in "task_overview.txt" and "user_overview.txt" and
print all data to the console in a neat and readable manner """


def display_stats():
    data = []
    if not os.path.exists("task_overview.txt"):
        gen_reports()

    with open("task_overview.txt", "r", encoding="utf-8-sig") as task_overview_file:
        for line in task_overview_file:
            data = line.split(", ")
            print("=" * 30)
            print("Task Overview:\n")
            print(f"Total tasks:           \t{data[0]}\n"
                  f"Complete:              \t{data[1]}\n"
                  f"Incomplete:            \t{data[2]}\n"
                  f"Overdue:               \t{data[3]}\n"
                  f"Percentage Incomplete: \t{data[4]}%\n"
                  f"Percentage Overdue:    \t{data[5]}%\n")
            print("=" * 30)

    print("User Overview: \n")
    with open("user_overview.txt", "r", encoding="utf-8-sig") as user_overview_file:
        i = 0
        for line in user_overview_file:
            i += 1
            if i > 3:
                print("=" * 30)
                data = line.split(", ")
                percentage_overdue = data[7].replace("\n", "")
                print(f"User:                     \t{data[0]}\n"
                      f"Total Tasks:              \t{data[1]}\n"
                      f"Total task percentage:    \t{data[4]}%\n"
                      f"Percentage Completed:     \t{data[5]}%\n"
                      f"Percentage Uncompleted:   \t{data[6]}%\n"
                      f"Percentage Overdue:       \t{percentage_overdue}%\n")
            else:
                print(line.replace("\n", ""))
        print("=" * 30)


"""Declare a dictionary for all the usernames and passwords.
Read data from file to dictionary reading the passwords as values
and the usernames as keys.
Request user input to provide username and password and check if there is
a match in the dictionary.
Once correct username with matching password is entered print menu to
console."""
users_dict = {}
with open("user.txt", "r", encoding="utf-8-sig") as users_file:
    for line in users_file:
        data = line.split(", ")
        users_dict[data[0]] = data[1].replace("\n", "")

print("=" * 30)
while True:
    username = input("Please enter a username: \n")
    print("=" * 30)
    if username in users_dict:
        password = input("Enter your password: \n")
        print("=" * 30)
        if password == users_dict[username]:
            break
        else:
            print("Password is incorrect!")
            print("=" * 30)
    else:
        print("Username is incorrect!")
        print("=" * 30)

"""Main while loop that requests input from user to select a option
from the menu below. If a wrong option was chosen print error
to console and as to choose again.
If 'e' is chosen the program will close.
'ds - Display Statistics'  'r - Register user'
and 'gr- generate reports' will only print for admin
Input is taken to lowercase to prevent errors"""

while True:
    print(("*" * 20) + "TASK MANAGER" + ("*" * 20) + "\n")
    print('''Select one of the following Options below:
 _______________________                 
|a  - Adding a task     |
|va - View all tasks    |
|vm - view my task      |''')
    if username == "admin":
        print("|ds - Display Statistics|\n"
              "|gr - Generate Reports  |\n"
              "|r  - Registering a user|\n"
              "|                       |")
    print("|e  - Exit              |")
    menu = input("|_______________________| \n\n>").lower()

    if menu == 'r':
        reg_user(username)
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine(username)
    elif menu == 'gr' and username == "admin":
        gen_reports()
    elif menu == 'ds' and username == "admin":
        display_stats()

    elif menu == 'e':
        print("=" * 30)
        print('Goodbye!!!')
        print("=" * 30)
        exit()

    else:
        print("=" * 30)
        print("You have made a wrong choice, Please Try again")
        print("=" * 30)