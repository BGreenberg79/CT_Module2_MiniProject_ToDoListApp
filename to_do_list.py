#To Do List Application

list_of_incomplete_tasks = []
list_of_complete_tasks = []

# Defines the two empty lists we will be adding, removing, and moving items to/from in our functions 

def main_menu_init():
    print("Welcome to our To-Do List App! \nMenu: \n1. Add a task \n2. View tasks \n3. Mark a task as complete \n4. Delete a task \n5. Quit")
    while True:
        ask_user = input("What option would you like to select today (1-5):")
        if ask_user == "1":
            print("You have selected to add a task")
            while True:
                ask_task = input("What would you like to add to your task list?: ").title()
                add_a_task(ask_task)
                continue_adding = input("Would you like to continue adding to the list? (yes/no): ").lower()
                if continue_adding == "yes":
                    continue
                if continue_adding == "no":
                    break
                if continue_adding != "yes" and continue_adding != "no":
                    print("Please respond yes or no. Reinitiatiing program.")
                    break
        if ask_user == "2":
            print("You have selected to view your tasks")
            view_tasks()
        if ask_user == "3":
            print("You have chosen to mark a task as complete")
            task_completed = input("Which task number has been completed?: ")
            mark_complete(task_completed)
        if ask_user == "4":
            print("You have chosen to delete a task")
            delete_list = input("Which list would you like to delete from? (incomplete/complete):  ")
            if delete_list == "incomplete":
                incomplete_task_to_delete = input("Which task number would you like to delete?: ").lower()
                task_delete_incomplete(incomplete_task_to_delete)
            if delete_list == "complete":
                complete_task_to_delete = input("Which task number would you like to delete?: ").lower()
                task_delete_complete(complete_task_to_delete)
            if delete_list != "complete" and delete_list != "incomplete":
                print("Please select one of the two options, complete or incomplete")
        if ask_user == "5":
            break
        if ask_user != "5" and ask_user != "4" and ask_user != "3" and ask_user != "2" and ask_user != "1":
            print("Error: Please enter a valid digit from 1-5 to navigate the menu")

'''
the main_menu_init function is the backbone of our application and when calls initializes a main menu which uses a while loop to continuously ask our users
if they want to add a item (default to incomplete) to their to do list, view their task lists, mark a task as complete, remove an item from their lists, or exit the program altogether
If the user responds to the first input of ask_user with 1 (add an item) it will then ask users a second input of what they would like to add to their list.
The input returns a string that we can then pass through our next function add_a_task, followed by asking for another input if they would like to continue adding or not.
If the user responds with 2 (view tasks) the view_tasks function is called. If the user responds with 3 (mark an item as complete) another input is taken where the task number they wish to mark as complete is requested, and then that input is 
passed through the mark_complete function. If the user responds with 4 (delete tasks) it will ask if the item they wish to delete is from the incomplete or complete lists. Based off of that response
if the user chooses incomplete they will ask which task number they wish to delete from the incomplete list and if they choose the complete list they will similarly be asked which task number they wish to be deleted from their completed list.
This response is then passed through either the task_delete_incomplete or task_delete_complete functions.
If the user responds with 5 (Quit) the while chain is broken. As a control if the user fails to respond with a number from 1-5 to the first input, an error message will show prompting the user to respond with a valid digit from 1-5.
'''

def add_a_task(task):
    global list_of_incomplete_tasks
    list_of_incomplete_tasks.append(task)
    print("Your Incomplete Tasks:")
    for num, item in enumerate(list_of_incomplete_tasks, 1):
        print(str(num) + ".", item)

'''
The add_a_task funtion passes the (task) parameter through the function by appending the task to the global list_of_incomplete tasks.
It then prints a header followed by your list of incomplete tasks by using python's enumerate function starting from 1. The main_menu_init function calls this function and uses an input to create an argument for the task parameter.
'''

def view_tasks():
    global list_of_incomplete_tasks
    global list_of_complete_tasks
    print("Your Incomplete Tasks:")
    for incomplete_num, incomplete_item in enumerate(list_of_incomplete_tasks, 1):
        print(str(incomplete_num) + ".", incomplete_item)
    print("Your Complete Tasks:")
    for complete_num, complete_item in enumerate(list_of_complete_tasks, 1):
        print(str(complete_num) + ".", complete_item)

# The view_task functions uses the global list_of_incomplete_tasks and global list_of_complete_tasks by printing each in a numbered list using the enumerate function and a for loop.

def mark_complete(complete_index):
    global list_of_incomplete_tasks
    global list_of_complete_tasks
    try:
        complete_index = int(complete_index) - 1
        completed_item = list_of_incomplete_tasks.pop(complete_index)
        list_of_complete_tasks.append(completed_item)
    except IndexError:
        print("This item has already been marked completed or hasn't been added yet")
    except ValueError:
        print("Please enter the number that corresponds to this item, only digits are accepted.")
    else:
        print(f"Item number {complete_index+1}, {completed_item}, has been completed.")
    finally:
        print("Your Incomplete Tasks:")
        for incomplete_num, incomplete_item in enumerate(list_of_incomplete_tasks, 1):
            print(str(incomplete_num) + ".", incomplete_item)
        print("Your Complete Tasks:")
        for complete_num, complete_item in enumerate(list_of_complete_tasks, 1):
            print(str(complete_num) + ".", complete_item)

'''
The mark complete function works by taking the global list_of_incomplete_tasks and global list_of_complete_tasks and first in a try block
converting the parameter complete_index from string to integer (to account for user inputs always starting as string) and subtracting 1 (to account for python indexes starting from 0).
Then also in the try block we try to assign to the variable completed_item the return that python's built-in pop function produces when it removes the item from list_of_incomplete_tasks that complete_index calls for.
Lastly we append that item to the list_of_complete tasks. We use a try block as we anticipate to potential exceptions. The first exception is for an IndexError if the user gives an item index that has already been marked as complete or 
has not been added yet. We also anticipate ValueErrors for when users enter in a string input instead of the numbered item from a list as only digits can be converted to integers and used in the pop function. In an else statement after our two exceptions we print
which item number and item has been marked as complete, and in a finally statement we reprint the full incomplete and complete task lists using the enumerate function as that will be helpful for the user regardless of if they used the app correctly or incorrectly.
'''

def task_delete_complete(complete_del_task_index):
    global list_of_complete_tasks
    global list_of_incomplete_tasks
    try:
        complete_del_task_index = int(complete_del_task_index) - 1
        print(f"Item number {complete_del_task_index+1}, {list_of_complete_tasks[complete_del_task_index]}, will be removed from your completed list now.")
        del list_of_complete_tasks[complete_del_task_index]
    except IndexError:
        print("Please ensure this number of items exists on your completed task list.")
    except ValueError:
        print("Please enter the number that corresponds to this item, only digits are accepted.")
    finally:
        print("Your Incomplete Tasks:")
        for incomplete_num, incomplete_item in enumerate(list_of_incomplete_tasks, 1):
            print(str(incomplete_num) + ".", incomplete_item)
        print("Your Complete Tasks:")
        for complete_num, complete_item in enumerate(list_of_complete_tasks, 1):
            print(str(complete_num) + ".", complete_item)

def task_delete_incomplete(incomplete_del_task_index):
    global list_of_incomplete_tasks
    global list_of_complete_tasks
    try:
        incomplete_del_task_index = int(incomplete_del_task_index) - 1
        print(f"Item number {incomplete_del_task_index+1}, {list_of_incomplete_tasks[incomplete_del_task_index]}, will be removed from your incomplete list now.")
        del list_of_incomplete_tasks[incomplete_del_task_index]
    except IndexError:
        print("Please ensure an this number of items exist on your incomplete task list.")
    except ValueError:
        print("Please enter the number that corresponds to this item, only digits are accepted.")
    finally:
        print("Your Incomplete Tasks:")
        for incomplete_num, incomplete_item in enumerate(list_of_incomplete_tasks, 1):
            print(str(incomplete_num) + ".", incomplete_item)
        print("Your Complete Tasks:")
        for complete_num, complete_item in enumerate(list_of_complete_tasks, 1):
            print(str(complete_num) + ".", complete_item)
        
'''
The functions task_delete_incomplete and task_delete_complete work nearly identically to our mark_complete function using all of the same logic
and structure in its try, except, and finally blocks. It protects against any index or value errors when the user calls for an item that hasn't been added to the complete or incomplete lists or enters in string when an integer is anticipated.
The only main difference in these two functions is that instead of using python's pop and append built in function's, we use python's del statements to remove the indexes specified once the user input argument is converted to integer and has been subtracted by 1 to account for Python's index starting at 0.
Here I also print an f string of what item number and item is being deleter prior to the actual delete statement is completed as once that information has been deleted from the program it can't be recalled in a statement for the user to see on the terminal.
'''
try:
    main_menu_init()
finally:
    print("Thank you for using our To-Do List App!")

'''
Here at the very bottom of the app after all of the logic has been built up and structured I finally call the main_menu_init function and get that initial while loop started.
I call it in a try block so I can put a finally statement right after it that will thank users for using our app.
'''