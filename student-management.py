students=[]
def add_student():
    name=input("Enter name:")
    roll=input("Enter roll no:")
    marks=input("Enter marks:")
    students.append({"name":name,"roll":roll,"marks":marks})
    print("Student added!\n")
def view_students():
    if len(students)==0:
        print("No students found\n") 
    for s in students:
        print(s)
def search_students():
    roll=input("Enter roll no to search:")
    for s in students:
        if s["roll"]==roll:
            print("Found:",s)
            return
        print("Not found\n")
def delete_student():
    roll=input("Enter roll no to delete:")
    for s in students:
        if s["roll"]==roll:
            students.removed(s)
            print("Deleted!\n")
    print("Not found\n")
    return    
while True:
    print("\n1.Add 2.View 3.Search 4.Delete 5.Exit")
    choice=input("Enter choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
        delete_student()
    elif choice=="5":
        break    
