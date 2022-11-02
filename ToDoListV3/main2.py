class ToDoListItem:
    ToDoList = []
    def __init__(self, item_description):
        self.item_description = item_description
        self.item_status = False

    def __str__(self):
        return "%d %s" % (self.item_description, self.item_status)

def main():

    print("If You Want To Add an Item to your list select - 1")
    print("If You Want To View your list select - 2")
    print("If You Want To Remove an item from your list select- 3")
    print("If You Want to Mark an item as complete - 4")
    print("If You Want to Mark an item as incomplete - 5")

main()
user_input = int(input("Select your action "))
while user_input != 0:
    if user_input == 1:
        user_input = input("Make an entry into your list ")
        ToDoListItem.ToDoList.append(user_input)
    elif user_input == 2:
        for item in ToDoListItem.ToDoList:
            print(item)
    elif user_input == 3:
        for item in ToDoListItem.ToDoList:
            print(item)
        delete_item = input("enter the item you want to be deleted ")
        if (delete_item in ToDoListItem.ToDoList):
            ToDoListItem.ToDoList.remove(delete_item)
            print("Your Entry has been deleted")
        else:
            print("Your Entry is not present in list")
    elif user_input == 4:
        complete_item = input("Mark an entry as complete in your list ")
        print("\nPrinting Complete List: ")
        for items in ToDoListItem.ToDoList:
            if items == complete_item:
                item_status = True
                print(items)
    elif user_input == 5:
        in_complete_item = input("Mark an entry as in-complete in your list ")
        print("\nPrinting In-Completed List: ")
        for items in ToDoListItem.ToDoList:
            if items == in_complete_item:
                item_status = False
                print(items)
    print()
    main()
    user_input = int(input("Select your action "))
