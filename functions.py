import os

# Function to add a task to the tasks list
def add_task(tasks):
    """
    Adds a new task to the task list.
    
    Args:
    tasks (list): The list of tasks to which the new task will be added.
    
    Returns:
    list: The updated list of tasks with the newly added task.
    """
    
    print("\n\n---- add task ----\n")
    
    title = input("Enter title of the task: ")
    description = input("Enter the discription of the task: ")
    
    # Generate a unique task ID
    try:
        task_id = int(tasks[len(tasks) - 4]) + 1
    except IndexError:
        task_id = 1
    task_id = str(task_id)
    
    # Append the task details to the tasks list
    tasks.append(task_id)
    tasks.append(title)
    tasks.append(description)
    tasks.append(False) # Initially, the task is not completed
    print("\nTask successfully added!\n\n" + "-" * 18 + "\n")
    return tasks

# Function to view tasks in the tasks list
def view_tasks(tasks):
    """
    Displays the list of tasks, including their status, title, and description.
    
    Args:
    tasks (list): The list of tasks to be displayed.
    """
    
    print("\n\n---- view tasks ----\n")
    for i in range(0, len(tasks)):
        if i % 4 == 0:
            if not tasks[i + 3]:
                print(tasks[i] + " [] ", end="")
            elif tasks[i + 3]:
                print(tasks[i] + " [ Done ] ", end="")
            print( tasks[i + 1] + " - " + tasks[i + 2] + ".")
    print("\n" + "-" * 18 + "\n")

# Function to mark a task as completed
def mark_completed(tasks):
    """
    Marks a task as completed based on user input.
    
    Args:
    tasks (list): The list of tasks to select a task for marking as completed.
    
    Returns:
    list: The updated list of tasks with the selected task marked as completed.
    """
    print("\n\n---- mark as completed ----\n")
    
    which = input("Enter which task by number: ")
    task_done = False
    
    # Find the task and mark it as completed
    for i in range(0, len(tasks)):
        if tasks[i] == which and i % 4 == 0:
            task_done, tasks[i + 3] = True, True
            break
    
    if task_done:
        print("\nTask successfully marked as completed!\n\n" + "-" * 18 + "\n")
    else:
        print("\nTask was not found!\nPlease make sure the number was right\n\n" + "-" * 18 + "\n")
        
    return tasks

# Function to remove a task from the tasks list
def remove_task(tasks):
    """
    Removes a task from the task list based on user input.
    
    Args:
    tasks (list): The list of tasks to select a task for removal.
    
    Returns:
    list: The updated list of tasks with the selected task removed.
    """
    print("\n\n---- remove task ----\n")
    which = input("Enter which task by number: ")
    
    down_by_1 = False
    deleted = 0
    
    # Find and delete the task
    for i in range(0, len(tasks) - 1):
        if tasks[i] == which and i % 4 == 0:
            del tasks[i]
            del tasks[i]
            del tasks[i]
            del tasks[i]
            down_by_1 = True
            deleted = i
            break
    
    # Adjust task IDs after deletion
    for i in range(0, len(tasks) - 1):
        if down_by_1 and i >= deleted and i % 4 == 0:
            tasks[i] = str(int(tasks[i]) - 1)
    
    if down_by_1:    
        print("\nTask successfully removed!\n\n" + "-" * 18 + "\n")
    else:
        print("\nTask was not found!\nPlease make sure the number was right\n\n" + "-" * 18 + "\n")
    return tasks


# Function to save tasks to a file and exit the program
def save_quit(tasks):
    """
    Saves the current list of tasks to a file and terminates the program.
    
    Args:
    tasks (list): The list of tasks to be saved to a file.
    
    Returns:
    bool: Always returns False to exit the program.
    """
    with open("tasks.txt", "w", encoding="utf-8") as f:
        for i in tasks:
            f.write(str(i) + "\n")
    return False

# Function to load tasks from a file and initialize the tasks list
def booting():
    """
    Initializes the task list from a file on program startup.
    
    Returns:
    list: The initial list of tasks loaded from a file (or an empty list if the file doesn't exist).
    """
    bool_map = {
        "True": True,
        "False": False,
    }
    tasks = list()
    
    # Check if a tasks file exists and load data if available
    if os.path.isfile("tasks.txt"):
        file = open("tasks.txt", "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
        
        for i in range(0, len(lines)):
            if i % 4 == 0 and i != 0:
                tasks[i - 1] = bool_map.get(lines[i - 1][:-1])
            if i == len(lines) - 1:
                tasks.append(bool_map.get(lines[i][:-1]))
                continue
            tasks.append(lines[i][:-1])

    return tasks