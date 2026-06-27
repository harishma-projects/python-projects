tasks=[]
def add_task():
    task=input("Enter task:")
    tasks.append(task)
    print("Task added!\n")
def view_tasks():
    if len(tasks)==0:
        print("No tasks found\n")
    else:
        print("\nYour Tasks:")
        for i,t in enumerate(tasks,start=1):
            print(i,t)
        print()
def delete_task():
    view_tasks()
    try:
        num=int(input("Enter task number to delete:"))
        tasks.pop(num-1)
        print("Task deleted!\n")
    except:
        print("Invalid input!\n")
while True:
    print("1.Add 2.View 3.Delete 4.Exit")
    choice=input("Enter choice:")
    if choice=="1":
        add_task()
    elif choice=="2":
        view_tasks()
    elif choice=="3":
        delete_task()
    elif choice=="4":
        break                                          