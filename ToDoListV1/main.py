to_do_list = []


def menu():
    print("If You Want To Add an Item to your list select - 1")
    print("If You Want To View your list select - 2")
    print("If You Want To Remove an item from your list select- 3")
    print("If You Want to Mark an item as complete/incomplete - 4")


menu()
user_input = int(input("Select your action "))
while user_input != 0:
    if user_input == 1:
        user_input = input("Make an entry into your list ")
        to_do_list.append(user_input)
        print("Your Entry has been added ")
    elif user_input == 2:
        print(to_do_list)
    elif user_input == 3:
        print(to_do_list)
        delete_item = input("enter the item you want to be deleted ")
        if (delete_item in to_do_list):
            to_do_list.remove(delete_item)
            print("Your Entry has been deleted")
        else:
            print("Your Entry is not present in list")
    elif user_input == 4:
        print(to_do_list)
        complete_item = input("enter the item you want to mark as complete ")
        if complete_item in to_do_list:
            search_item_index = to_do_list.index(complete_item)
            to_do_list[search_item_index] += "-completed"
            print(to_do_list)
        else:
            print("Your Entry is not present in list")

    print()
    menu()
    user_input = int(input("Select your action"))