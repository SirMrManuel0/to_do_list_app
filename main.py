# Import necessary functions and modules
import functions
import os

# Initialize the 'tasks' list by calling the 'booting' function
tasks = functions.booting()

# Define the standard menu options
standard = "\n\nWelcome to the To-Do List App!\n\n" + \
        "1. Add Task\n" \
        "2. View Tasks\n" \
        "3. Mark as Completed\n" \
        "4. Remove Task\n" \
        "5. clear\n" \
        "6. Save and Quit\n\n"
print(standard)

# Initialize a loop to keep the program running
on = True


while on:
    # Get user input for menu choice
    user_input = input("Enter your choice: ")
    
    if user_input == "1":
        # Call the 'add_task' function to add a task to the 'tasks' list
        tasks = functions.add_task(tasks)
    elif user_input == "2":
        # Call the 'view_tasks' function to display the tasks
        functions.view_tasks(tasks)
    elif user_input == "3":
        # Call the 'mark_completed' function to mark a task as completed
        tasks = functions.mark_completed(tasks)
    elif user_input == "4":
        # Call the 'remove_task' function to remove a task from the 'tasks' list
        tasks = functions.remove_task(tasks)
    elif user_input == "5":
        # Clear the screen and display the standard menu again
        os.system('cls' if os.name == 'nt' else 'clear')
        print(standard)
    elif user_input == "6":
        # Call the 'save_quit' function to save tasks and exit the program
        on = functions.save_quit(tasks)
    else:
        # Display an error message for invalid input
        print("\nWrong input!\nPlease only enter the number corresponding what you want to do.\n")