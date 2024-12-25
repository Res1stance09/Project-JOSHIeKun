#TOdo list

def list():
    print("\n TO DO LIST STATEMENT!")
    print("1. VIEW A LIST!")
    print("2. Add a list")
    print("3. Remove list ")
    print("4. Quit")

def viewlist(todo_list):
    if todo_list is None:
        print("your todo list empty")
    else:
        print("\n Your to do list")
        for x,y in enumerate(todo_list, start=1):
            print(f"{x}.{y}")

def add_list(todo_list):
    additem = input("Enter an item to add: ")
    todo_list.append(additem)
    print(f" '{additem}' Has added to your list")

def remove_item(todo_list):
    try:
        viewlist(todo_list)
        x = int(input("Enter a list to remove: "))- 1
        remove_item = todo_list.pop(x)
        print(f" '{remove_item}', has been removed to your list!")
    except (IndexError,ValueError):
        print("Invalid Expression pls try again")

def main():
    todo_list = []
    while True:
        list()
        choice = input("Choose the list to the top!: ")
        if choice == "1":
            viewlist(todo_list)
        elif choice == "2":
            add_list(todo_list)
        elif choice == "3":
            remove_item(todo_list)
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choices must 1 to 4 only!")
if __name__ == "__main__":
    main()