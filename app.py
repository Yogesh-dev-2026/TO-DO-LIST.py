todo_list = []

while True:
    print("To-do List Application Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        if not todo_list:
            print("\Your to-do list is empty!")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(todo_list,start =1):
                print(f"{index}.{task}")

    elif choice =="2":
        new_task = input("Enter the task description:")
        if new_task.strip() != "":
            todo_list.append(new_task)
            print(f"Task "{new_task}" added to the list.")
        else:
            print("Task description cannot be empty!")

    elif choice =="3":
        if not todo_list:
            print("Your todo_lsit is empty! NOthing to remove ")
        else:
            print("\nYour Tasks:")
            for index ,tasks in enumerate(todo_list, start=1):
                print(f"{index}. {tasks}")
     
            try:
                task_num = int(input("\nEnter the number of tasks to delete:"))
                if  1<=task_num <= len(todo_list):
                    removed_task = todo_list.pop(task_num - 1)
                    print(f"Task "{removed_task}" has been removed from the list.")
                else:
                    print("Invalid task number.") 

            except ValueError:
                print("Please enter a valid number.")
                