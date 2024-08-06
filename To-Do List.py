def main():
    tasks = []    # creating a list
# display menubar
    while 1:
        print("\n***** To-Do List *****")
        print("1. Add Task")
        print("2. Show Task")
        print("3. Remove Task")
        print("4. Mark Task as Done")
        print("5. Exit")
# take input from user
        choice = input("Give your choice: ")
# Add task in list
        if choice == '1':
            print()
            n_tasks = int(input("How may task you want to add in list: "))

            for i in range(n_tasks):
                task = input("Enter the task name: ")
                tasks.append({"task": task, "done": False})
                print("Task added successfully...!")
# show task which are added in list
        elif choice == '2':
            print("\nTasks:")
            if len(tasks) != 0:
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")
            else:
                print("\nList is Empty..")
# mark as task completed
        elif choice == '4':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done..!")
            else:
                print("Task not found..!!.")
# delete task from list
        elif choice == '3':
            n = int(input("Enter task number,which you want to delete.?"))
            if 0 <= n < len(tasks):
                tasks.pop(n)
                print("\nDeleted successfully done..!!")
            else:
                print("\nTask not found..!!")
# exit
        elif choice == '5':
            print("Thank you..!!")
            break
        else:
            print("Invalid choice..!!\nPlease give correct input from list.")


if __name__ == "__main__":
    main()
