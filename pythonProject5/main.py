class Todolist:
    listoftasks = []
    completedtasks = []
    incompletetasks = []

   # Initialises user inputs ID, and description in Todo List class
    def __init__(self, item_id, item_description):
        self.item_id = item_id
        self.item_description = item_description

    # Adds user input in todo List
    def addNewTask(self):
        Todolist.listoftasks.append(self)

    # returns list of todo tasks
    def getTaskList(self):
        return Todolist.listoftasks

    # returns list of completed tasks
    def getCompletedTasks(self):
        return Todolist.completedtasks

    # returns list of incomplete tasks
    def getIncompleteTasks(self):
        return Todolist.incompletetasks

    # updates entry in the list by first checking items in the list,
    # then matches user input with the ID of an exiting item in the list, then updates the ID and description
    def updateListEntry(self, item_id, item_description):
        for item in Todolist.listoftasks:
            if (item.getItemId() == item_id):
                item.item_id = item_id
                item.item_description = item_description
                return True
        return False

    # removes entry in the list by first checking items in the list,
    # then matches user input with the ID of an exiting item in the list, then removes the element
    def removeListEntry(self, item_id):
        for item in Todolist.listoftasks:
            if (item.getItemId() == item_id):
                Todolist.listoftasks.remove(item)
                return True
        return False

   # adds an entry in the list of complete/incomplete tasks based on the selection made by the user
   # for both complete/incomplete lists the function first checks the items in the To Do list
   # then matches user input with the ID of an exiting item in the To Do list
   # then appends/moves the entry in complete/incomplete lists, and at the end removes the input from to do list
    def markListEntry(self, item_id):
        print(" Mark as complete -a \n Mark as incomplete-b")
        selection = input("Enter you option: ")

        if selection == "a":
            for item in Todolist.listoftasks:
                if (item.getItemId() == item_id):
                    Todolist.completedtasks.append(item)
                    Todolist.listoftasks.remove(item)
                    return True
            return False

        if selection == "b":
            for item in Todolist.listoftasks:
                if (item.getItemId() == item_id):
                    Todolist.incompletetasks.append(item)
                    Todolist.listoftasks.remove(item)
                    return True
            return False

    # returns item ID
    def getItemId(self):
        return self.item_id

    # returns item description
    def getItemDescription(self):
        return self.item_description

    # returns class objects, item ID and description as strings
    def __str__(self):
        return "%d %s" % (self.item_id, self.item_description)


choice = 1
placeholder_list = Todolist(0, "")
while choice >= 1 and choice <= 7:
    print(
        " Add New Entry -1 \n Show List -2 \n Update an entry in the list -3 \n Remove an entry from list -4 \n Mark and item as complete/Incomplete -5 \n Show completed list -6 \n show incomplete list -7")
    choice = int(input("Enter you option: "))
    if choice == 1:
        item_id = int(input("Enter List ID: "))
        item_description = input("Enter Description: ")
        call_todolist = Todolist(item_id, item_description)
        call_todolist.addNewTask()
    elif choice == 2:
        for item in placeholder_list.getTaskList():
            print(item)

    elif choice == 3:
        item_id = int(input("Enter List ID: "))
        item_description = input("Enter Description: ")
        call_todolist = placeholder_list.updateListEntry(item_id, item_description)
        if call_todolist == False:
            print("\n Entry not found, failed to update")
        else:
            print("\n Entry updated")
    elif choice == 4:
        item_id = int(input("Enter List ID: "))
        call_todolist = placeholder_list.removeListEntry(item_id)
        if call_todolist == False:
            print("\n Entry not found, failed to remove")
        else:
            print("\n Entry successfully removed")
    elif choice == 5:
        item_id = int(input("Enter List ID: "))
        call_todolist = placeholder_list.markListEntry(item_id)
        if call_todolist == False:
            print("\n Entry not found, failed to mark")
        else:
            print("\n Entry successfully marked")
    elif choice == 6:
        for item in placeholder_list.getCompletedTasks():
            print(item)

    elif choice == 7:
        for item in placeholder_list.getIncompleteTasks():
            print(item)