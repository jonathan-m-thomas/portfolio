import json

# File to store tasks
# This is where all the tasks will be stored
# the actual data will be stored in a json file, but when it is loaded into the program, it will be converted to a Python list.
data_file = "tasks.json"
# note that tasks in this program will be individual dictionaries stored within a single List, in the context of the methods defined below.
# to save tasks, they get dumped into the json file
# to actually work with and reference tasks in this program, the tasks themselves are each a dictionary, reference within a Python list.
# so, index 0 of tasks, or tasks[0], would reference the first dictionary, which is how we're defining tasks.
 

# Load tasks from file
def load_tasks():
    try: # load_tasks will be a function that can be called whenever
        with open(data_file, "r") as file: # "with" is a helper statement. # open(data_file, "r") opens the file in read mode. "with" ensures the file will be closed properly when done.
            return json.load(file) # return the actual file we loaded. It will be a JSON object. These are used to store data often. json.load(file) will read the content of the file 
    except FileNotFoundError: # and it will then convert the file to Python object such as a list in this case.
        return []

# Save tasks to file
def save_tasks(tasks): # pass tasks into this function as input. tasks will be a Python list
    with open(data_file, "w") as file: #takes input which will be a Python List. This is how the tasks are saved while the program is running. 
        json.dump(tasks, file, indent=4)
        # once the program is done, the tasks are saved using "with" which is a helper funciton that makes sure the file is closed properly after we are done writing to it, open(data_file, "w") which opens the file in write mode
        # json.dump(tasks, file, indent=4) literally just dumps the info into the file. It is from the json library which was imported at the top of this program.
        # indent=4 just gives 4 white spaces to make it a little easier to read

# Display tasks
def display_tasks(tasks):
    if not tasks: # if "not tasks", meaning, if the task list is empty, then tell the user there are no tasks.
        print("\nNo tasks available!\n")
        return # get out of the function, nothing to see here if there were no tasks.

    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, 1): # iterate through the tasks. the "1" here just starts the list at 1 rather than 0 for readability. 
        status = "[x]" if task["completed"] else "[ ]" # tasks is iterable, so we can use the enumerate(iterable, start=0) function on it. It will iterate over the tasks and give an index/idx for each one.
        print(f"{idx}. {status} {task['title']} (Due: {task['due_date'] or 'No due date'})") # print the tasks nice and neat

# Add a task
def add_task(tasks):
    title = input("Enter task title: ")
    due_date = input("Enter due date (optional): ")
    tasks.append({"title": title, "due_date": due_date, "completed": False}) #tasks is a List of dictionary entries. 
    print("Task added successfully!\n")

# Mark a task as complete
def complete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as complete: "))
        tasks[task_num - 1]["completed"] = True
        print("Task marked as complete!\n")
    except (ValueError, IndexError):
        print("Invalid task number!\n")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        tasks.pop(task_num - 1)
        print("Task deleted successfully!\n")
    except (ValueError, IndexError):
        print("Invalid task number!\n")

# Modify a task
def modify_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter task number to update a task: "))
        # ask user which task they want to edit
        task = tasks[task_num -1] # adjust for 0-based index since task_num starts at. here, "task" will store a reference to the item in the python list dictionary 
        
        # show selected task details
        print(f"\nCurrent Task Details:")
        print(f"Title: {task['title']}")
        print(f"Due Date: {task['due_date'] or 'No due date'}")
        print(f"Completed: {'Yes' if task['completed'] else 'No'}")

        # what does the user want to update?
        print("\nWhat would you like to update?")
        print("1. Title")
        print("2. Due Date")
        print("3. Completion Status")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            new_title = input("Enter new title: ")
            task["title"] = new_title
            print("Task title updated successfully!")
        elif choice == "2":
            new_due_date = input("Enter new due date (or press Enter to clear): ")
            task["due_date"] = new_due_date if new_due_date.strip() else None
            print("Task due date updated successfully!")
        elif choice == "3":
            new_status = input("Mark task as completed? (yes/no): ").strip().lower()
            if new_status in ("yes", "y"):
                task["completed"] = True
            elif new_status in ("no", "n"):
                task["completed"] = False
            else:
                print("Invalid input for completion status!")
            print("Task completion status updated successfully!")
        else:
            print("Invalid choice. No changes were made.")

    except (ValueError, IndexError):
        print("Invalid selection. Please try again.")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Modify a task.")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            modify_task(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
