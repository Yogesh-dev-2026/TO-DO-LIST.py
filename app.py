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
        task = input("Enter the task description:")
        todo_list.append(task)
        print(f"Task "{Task}" added to the list.")

   

     
