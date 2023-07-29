import functions
import os

tasks = functions.booting()

standard = "\n\nWelcome to the To-Do List App!\n\n" + \
        "1. Add Task\n" \
        "2. View Tasks\n" \
        "3. Mark as Completed\n" \
        "4. Remove Task\n" \
        "5. clear\n" \
        "6. Save and Quit\n\n"
print(standard)

on = True


while on:
    user_input = input("Enter your choice: ")
    if user_input == "1":
        tasks = functions.add_task(tasks)
    elif user_input == "2":
        functions.view_tasks(tasks)
    elif user_input == "3":
        tasks = functions.mark_completed(tasks)
    elif user_input == "4":
        tasks = functions.remove_task(tasks)
    elif user_input == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(standard)
    elif user_input == "6":
        on = functions.save_quit(tasks)
    else:
        print("\nWrong input!\nPlease only enter the number corresponding what you want to do.\n")