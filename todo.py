todo_list = []

def addList():
    item = input("Enter a new Task:")
    todo_list.append(item)
    print(f"{item} added to the to-do list")

def displayList():
    print("-------------")
    print("To Do List:")
    print("-------------")
    for index, item in enumerate(todo_list, start=1):
        print(f"{index} - {item}")

def removeList():
    if not todo_list:
        print("The list is already empty!")
        return
    displayList()
    index = int(input("Enter the item to be removed: ")) - 1
    
    if 0 <= index < len(todo_list):
        removed_item = todo_list.pop(index)
        print(f"{removed_item} removed from the list")
    else:
        print("Invalid Input")

while True:
    print("\n\n#################\n\n")
    print("To Do List App\n")
    print("1 - Add To List")
    print("2 - Display List")
    print("3 - Remove from list")
    print("4 - Exit\n")

    option = input("Select your Option: ")

    if option == '1':
       addList()
    elif option == '2':
       displayList()
    elif option == '3':
        removeList()
    elif option == '4':
        print("EXIT\n")
        break
    else:
        print("INVALID Option")
