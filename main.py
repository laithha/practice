
'''Add item → ask the user for an item and add it to the list.

List items → print all the items.

Delete item → ask which item to remove, and delete it if it exists.

Update item → replace an existing item with a new one.

Search item → check if an item is in the list.

This way, you practice the same concepts as before but with strings instead of numbers.'''
items = []
def additem():
    item = input("enter the item you want to add: ")
    items.append(item)
    print(items)

def listitems():
    if not items:
        print("there is no items in the database")
    print(items)

def deleteitem():
    name = input("enter the item that you want to delete:")
    if name in items:
        items.remove(name)
    else:
        print("there is no succh thing in the database")

def updateitem():
    item = input("what is the item that you want to update:")
    if item in items:
        item1 = input("enter the new item:")
        item2 = items.index(item)
        items[item2] = item1

def searchitem():
    item = input("enter the item that you want to search which will print only the name ")
    if item in items:
        print("found: ", item)
    else:
        print("the item is not in the database")

while True:
    print("WELCOME TO LAITH'S shopping manager")
    print("1.Add item")
    print("2.List all items")
    print("3.delete item")
    print("4.update item ")
    print("5.search for item")
    print("6.exit")
    choice = int(input("choose: "))
    if choice == 1:
        additem()
    elif choice == 2:
        listitems()
    elif choice == 3:
        deleteitem()
    elif choice == 4:
        updateitem()
    elif choice == 5:
        searchitem()
    elif choice == 6:
        break