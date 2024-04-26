# Function to add a task to the task list
def add_task(task_list, task):
    task_list.append(task)
    print(f"Task '{task}' added.")

# Function to remove a task from the task list
def remove_task(task_list, task_index):
    if 0 <= task_index < len(task_list):
        removed_task = task_list.pop(task_index)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number.")

# Function to display the current tasks in the task list
def display_tasks(task_list):
    if not task_list:
        print("Task list is empty.")
    else:
        print("\nCurrent Tasks:")
        for i, task in enumerate(task_list):
            print(f"{i}: {task}")

# Main function where the program starts execution
def main():
    task_list = []

    print(
        """
        Type in a new task to add to the list.
        Type 'remove' to remove a task.
        Type 'done' to exit.
        """
    )

    # Loop to continuously interact with the user until the program is exited
    while True:
        # Get user input
        user_input = input("What would you like to do? ").strip().lower()

        # Check user input and take appropriate actions
        if user_input == "done":
            print("Goodbye!")
            break
        elif user_input == "remove":
            display_tasks(task_list)
            try:
                task_index = int(input("Enter the number of the task to remove: "))
                remove_task(task_list, task_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif user_input:
            add_task(task_list, user_input)
        else:
            print("Please type a task you haven't done yet.")

        display_tasks(task_list)

# Check if the script is being run directly
if __name__ == "__main__":
    main()
