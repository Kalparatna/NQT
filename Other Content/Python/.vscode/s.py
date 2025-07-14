# Initialize an empty to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to view the current to-do list
def view_list():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

while True:
    # Display menu
    print("\nMenu:")
    print("1. Add a task")
    print("2. View the to-do list")
    print("3. Quit")
    
    # Get user input for menu choice
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        task = input("Enter the task you want to add: ")
        add_task(task)
    elif choice == "2":
        view_list()
    elif choice == "3":
        print("Exiting the to-do list manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
