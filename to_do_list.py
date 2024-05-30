#To Do List Application

list_of_incomplete_tasks = []
list_of_complete_tasks = []

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


def add_a_task(task):
    global list_of_incomplete_tasks
    list_of_incomplete_tasks.append(task)
    print("Your Incomplete Tasks:")
    for num, item in enumerate(list_of_incomplete_tasks, 1):
        print(str(num) + ".", item)

def view_tasks():
    global list_of_incomplete_tasks
    global list_of_complete_tasks
    print("Your Incomplete Tasks:")
    for incomplete_num, incomplete_item in enumerate(list_of_incomplete_tasks, 1):
        print(str(incomplete_num) + ".", incomplete_item)
    print("Your Complete Tasks:")
    for complete_num, complete_item in enumerate(list_of_complete_tasks, 1):
        print(str(complete_num) + ".", complete_item)

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
        

try:
    main_menu_init()
finally:
    print("Thank you for using our To-Do List App!")