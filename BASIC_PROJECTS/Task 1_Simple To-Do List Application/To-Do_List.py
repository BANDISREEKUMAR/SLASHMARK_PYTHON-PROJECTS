tasks = []

def display():
    if not tasks:
        print("Your todo list is empty")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not done"
            print(f"{i}) {task['task']} ({status})")

def add_task(task_name):
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    print(f"Task '{task_name}' is added successfully:)")

def mark(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} is marked as completed")
    else:
        print("Entered number is not there in the list")

def remove(task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' is removed:<")
    else:
        print("Entered number is not there in the list:<")

while True:
    print("\nOperations to be performed with todo list")
    print("1. Display")
    print("2. Add a task")
    print("3. Mark a task as complete")
    print("4. Remove a task")
    print("5. Quit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        display()
    elif choice == '2':
        task_name = input("Enter a task: ")
        add_task(task_name)
    elif choice == '3':
        try:
            task_number = int(input("Enter a task number: "))
            mark(task_number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '4':
        try:
            task_number = int(input("Enter a task number: "))
            remove(task_number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '5':
        break
    else:
        print("Invalid operation")
