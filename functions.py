import os

def add_task(tasks):
    print("\n\n---- add task ----\n")
    
    title = input("Enter title of the task: ")
    description = input("Enter the discription of the task: ")
    
    try:
        task_id = int(tasks[len(tasks) - 4]) + 1
    except IndexError:
        task_id = 1
    task_id = str(task_id)
    tasks.append(task_id)
    tasks.append(title)
    tasks.append(description)
    tasks.append(False)
    print("\nTask successfully added!\n\n" + "-" * 18 + "\n")
    return tasks

def view_tasks(tasks):
    print("\n\n---- view tasks ----\n")
    for i in range(0, len(tasks)):
        if i % 4 == 0:
            if not tasks[i + 3]:
                print(tasks[i] + " [] ", end="")
            elif tasks[i + 3]:
                print(tasks[i] + " [ Done ] ", end="")
            print( tasks[i + 1] + " - " + tasks[i + 2] + ".")
    print("\n" + "-" * 18 + "\n")

def mark_completed(tasks):
    print("\n\n---- mark as completed ----\n")
    
    which = input("Enter which task by number: ")
    task_done = False
    
    for i in range(0, len(tasks)):
        if tasks[i] == which and i % 4 == 0:
            task_done, tasks[i + 3] = True, True
            break
    
    if task_done:
        print("\nTask successfully marked as completed!\n\n" + "-" * 18 + "\n")
    else:
        print("\nTask was not found!\nPlease make sure the number was right\n\n" + "-" * 18 + "\n")
        
    return tasks

def remove_task(tasks):
    print("\n\n---- remove task ----\n")
    which = input("Enter which task by number: ")
    
    down_by_1 = False
    deleted = 0
    
    for i in range(0, len(tasks) - 1):
        if tasks[i] == which and i % 4 == 0:
            del tasks[i]
            del tasks[i]
            del tasks[i]
            del tasks[i]
            down_by_1 = True
            deleted = i
            break
    
    for i in range(0, len(tasks) - 1):
        if down_by_1 and i >= deleted and i % 4 == 0:
            tasks[i] = str(int(tasks[i]) - 1)
    
    if down_by_1:    
        print("\nTask successfully removed!\n\n" + "-" * 18 + "\n")
    else:
        print("\nTask was not found!\nPlease make sure the number was right\n\n" + "-" * 18 + "\n")
    return tasks
    
def save_quit(tasks):
    with open("tasks.txt", "w", encoding="utf-8") as f:
        for i in tasks:
            f.write(str(i) + "\n")
    return False

def booting():
    bool_map = {
        "True": True,
        "False": False,
    }
    tasks = list()
    
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