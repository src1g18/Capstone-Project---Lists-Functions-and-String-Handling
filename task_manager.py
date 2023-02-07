#=====importing libraries===========
import datetime

#=====importing libraries===========
import datetime

# File I created (task_manager_art.py) to keep graphics and embellishment for menus. Find the file in the same folder
from task_manager_art import welcome_message, admin_menu, bottom_line, user_menu, login_line, add_user_line, \
     wrong_user, wrong_password, failed_login, new_task_line, goodbye

#====Login Section====

print(welcome_message)

# Creating dictionary to  hold user credentials then reading the file that holds usernames and passwords
user_credentials = {}
with open('user.txt', 'r') as user_file_in:
    # separating username from password and adding them as key value pair in dictionary
    for line in user_file_in:
       username = line.split(',')[0]
       password = line.split(',')[-1].strip()
       user_credentials[username]=password

# Checking if the username and password combination is valid
while True:
    print(login_line)
    username = input("Username: ")
    if username in user_credentials:
        password = input("Password: ")
        if (username, password) in user_credentials.items():
            print(bottom_line)
            break
        else:
           print(failed_login)
    else:
       print(wrong_user)

# Presenting the menu to the users
while True:
    # Making sure that the user input is converted to lower case for comparisons.
    if username.lower() == "admin":
        print(admin_menu)
        menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
s - Statistics
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
    # Presenting a reduced menu to the non admin users
    else:
        print(user_menu)
        menu = input('''\nSelect one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
    # Only allowing the admin user to register new users, even if another user types r
    if menu == 'r' and username.lower() == "admin":
        while True:
            print(add_user_line)
            new_user = input("Username: ")
            # Getting password and confirming if they match
            while True:
                password = input("Password: ")
                password_retype = input("Retype Password: ")
                print(bottom_line)
                if password != password_retype:
                   print(wrong_password)
                else:
                    break
            break

        # Writing the  username/password to file
        user_file_out = open('user.txt', 'a')
        user_file_out.write("\n" + new_user + ", " + password)
        user_file_out.close()


    elif menu == 'a':
        print(new_task_line)
        # User Input
        task_title = input("Task Title:\t\t\t")
        task_user = input("User Assigned:\t\t\t")
        task_description = input("Task description:\t\t")
        task_due_date = input("Due date in dd/MM/YYYY:\t\t")
        task_complete = input("Task complete (Yes or No):\t")
        print(bottom_line)
        # Date Operations
        # Getting current date and formatting it accordingly
        current_date = datetime.datetime.now().strftime("%d %b %Y")
        # Converting user input into date format
        task_due_date = datetime.datetime.strptime(task_due_date, '%d/%m/%Y')
        # Converting user date into a string in the required format
        converted_due_date = task_due_date.strftime("%d %b %Y")
        # Writing To File
        task_file_out = open('tasks.txt', 'a')
        task_file_out.write("\n" + task_user + ", " + task_title + ", " + task_description + ", " + current_date +  ", " + converted_due_date + ", " + task_complete)
        task_file_out.close()

    elif menu == 'va':
        with open('tasks.txt', 'r') as tasks_file_in:
            for count, line in enumerate(tasks_file_in):
                print(f'''
────[TASK {count + 1}]────────────────────────────────────────────────────
Task:               {line.split(',')[1].strip()}
Assigned To:        {line.split(',')[0].strip()}
Date Assigned:      {line.split(',')[3].strip()}
Due Date:           {line.split(',')[-2].strip()}
Task Complete:      {line.split(',')[-1].strip()}
Task Description:
 {line.split(',')[2].strip()}
{bottom_line}  ''')

    elif menu == 'vm':
        with open('tasks.txt', 'r') as tasks_file_in:
            count = 0
            for line in tasks_file_in:
                # Checking if the task user matches the currently logged user
                if (line.split(',')[0].strip().lower() == username.lower()):
                    count += 1
                    print(f'''
────[TASK {count}]────────────────────────────────────────────────────
Task:               {line.split(',')[1].strip()}
Assigned To:        {line.split(',')[0].strip()}
Date Assigned:      {line.split(',')[3].strip()}
Due Date:           {line.split(',')[-2].strip()}
Task Complete:      {line.split(',')[-1].strip()}
Task Description:
 {line.split(',')[2].strip()}
{bottom_line} ''')

            if count == 0:
                print(f'''
────[TASK {count}]────────────────────────────────────────────────────
You don't have tasks assigned at the moment !
{bottom_line}
                ''')

    elif menu == 'e':
        print(goodbye)
        exit()

    elif menu == 's' and username.lower() == "admin":
        with open('tasks.txt', 'r') as tasks_file:
            tasks_file_count = len(tasks_file.readlines())

        with open('user.txt', 'r') as users_file:
            users_file_count = len(users_file.readlines())

        print(f'''
────[STATISTICS]────────────────────────────────────────────────
Total User Count:   {users_file_count}
Totals Task Count:  {tasks_file_count}
{bottom_line}
        ''')

    else:
        print("You have made a wrong choice, Please Try again")

#====Login Section====



# Creating dictionary to  hold user credentials then reading the file that holds usernames and passwords
user_credentials = {}
with open('user.txt', 'r') as user_file_in:
    # separating username from password and adding them as key value pair in dictionary
    for line in user_file_in:
       username = line.split(',')[0]
       password = line.split(',')[-1].strip()
       user_credentials[username]=password

# Checking if the username and password combination is valid
while True:
    print(login_line)
    username = input("Username: ")
    if username in user_credentials:
        password = input("Password: ")
        if (username, password) in user_credentials.items():
            print(bottom_line)
            break
        else:
           print(failed_login)
    else:
       print(wrong_user)

# Presenting the menu to the users
while True:
    # Making sure that the user input is converted to lower case for comparisons.
    if username.lower() == "admin":
        print(admin_menu)
        menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
s - Statistics
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
    # Presenting a reduced menu to the non admin users
    else:
        print(user_menu)
        menu = input('''\nSelect one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
    # Only allowing the admin user to register new users, even if another user types r
    if menu == 'r' and username.lower() == "admin":
        while True:
            print(add_user_line)
            new_user = input("Username: ")
            # Getting password and confirming if they match
            while True:
                password = input("Password: ")
                password_retype = input("Retype Password: ")
                print(bottom_line)
                if password != password_retype:
                   print(wrong_password)
                else:
                    break
            break

        # Writing the  username/password to file
        user_file_out = open('user.txt', 'a')
        user_file_out.write("\n" + new_user + ", " + password)
        user_file_out.close()


    elif menu == 'a':
        print(new_task_line)
        # User Input
        task_title = input("Task Title:\t\t\t")
        task_user = input("User Assigned:\t\t\t")
        task_description = input("Task description:\t\t")
        task_due_date = input("Due date in dd/MM/YYYY:\t\t")
        task_complete = input("Task complete (Yes or No):\t")
        print(bottom_line)
        # Date Operations
        # Getting current date and formatting it accordingly
        current_date = datetime.datetime.now().strftime("%d %b %Y")
        # Converting user input into date format
        task_due_date = datetime.datetime.strptime(task_due_date, '%d/%m/%Y')
        # Converting user date into a string in the required format
        converted_due_date = task_due_date.strftime("%d %b %Y")
        # Writing To File
        task_file_out = open('tasks.txt', 'a')
        task_file_out.write("\n" + task_user + ", " + task_title + ", " + task_description + ", " + current_date +  ", " + converted_due_date + ", " + task_complete)
        task_file_out.close()

    elif menu == 'va':
        with open('tasks.txt', 'r') as tasks_file_in:
            for count, line in enumerate(tasks_file_in):
                print(f'''
────[TASK {count + 1}]────────────────────────────────────────────────────
Task:               {line.split(',')[1].strip()}
Assigned To:        {line.split(',')[0].strip()}
Date Assigned:      {line.split(',')[3].strip()}
Due Date:           {line.split(',')[-2].strip()}
Task Complete:      {line.split(',')[-1].strip()}
Task Description:
 {line.split(',')[2].strip()}
{bottom_line}  ''')

    elif menu == 'vm':
        with open('tasks.txt', 'r') as tasks_file_in:
            count = 0
            for line in tasks_file_in:
                # Checking if the task user matches the currently logged user
                if (line.split(',')[0].strip().lower() == username.lower()):
                    count += 1
                    print(f'''
────[TASK {count}]────────────────────────────────────────────────────
Task:               {line.split(',')[1].strip()}
Assigned To:        {line.split(',')[0].strip()}
Date Assigned:      {line.split(',')[3].strip()}
Due Date:           {line.split(',')[-2].strip()}
Task Complete:      {line.split(',')[-1].strip()}
Task Description:
 {line.split(',')[2].strip()}
{bottom_line} ''')

            if count == 0:
                print(f'''
────[TASK {count}]────────────────────────────────────────────────────
You don't have tasks assigned at the moment !
{bottom_line}
                ''')

    elif menu == 'e':
        print(goodbye)
        exit()

    elif menu == 's' and username.lower() == "admin":
        with open('tasks.txt', 'r') as tasks_file:
            tasks_file_count = len(tasks_file.readlines())

        with open('user.txt', 'r') as users_file:
            users_file_count = len(users_file.readlines())

        print(f'''
────[STATISTICS]────────────────────────────────────────────────
Total User Count:   {users_file_count}
Totals Task Count:  {tasks_file_count}
{bottom_line}
        ''')

    else:
        print("You have made a wrong choice, Please Try again")