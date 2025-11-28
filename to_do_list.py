task_list = []
print("----Hello Welcome To Your To-Do Task Diary----\n")
def menu():
    choice = input("\nEnter Task : \n1 - Add Task.\n2 - View Task.\n3 - Delete Task.\nAnything For Exit.\n")
    return choice
def add_task(a):
    task_list.append(a)
def view_task():
    count = 1
    print("\nYour Task To do is : ")
    for i in task_list:
        print(f"{count} - {i}")
        count+=1
def del_task(a):
    for i in task_list:
        if i.lower() == a.lower():
            task_list.remove(i)
            print(f"Task {i} Deleted Successfully..")
        else:
            print("The Task Is Not in Diary You Want to Delete.")
while True:
    choice = menu()
    if choice == '1':
        a = input("Enter Your Task To Add in Diary : \n")
        add_task(a)
    elif choice == '2':
        view_task()
    elif choice == '3':
        a = input("Enter Task You Want to Delete : ")
        del_task(a)
    else:
        print("Thank You. Comeback Again Later.❤️")
        break