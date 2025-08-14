dinosaur = {}

def deleteDino():
    name = input("what is the name of the dino that you want to delete:")
    if name in dinosaur:
         dinosaur.pop(name)
    else:
         print("the dinosaur does not exist in the zoo")

def Adddino():
        key = input("Enter name: ")
        value = input("Enter age: ")
        dinosaur.setdefault(key, value)
        print(dinosaur)

def listDinosaurs ():
    if not dinosaur:
            print("there is no dino's in the database")
    print(dinosaur)

def updateDino():
    name = input("what is the dino's name that you want to update: ")
    if name in dinosaur:
          age = int(input("new age:"))
          dinosaur[name] = age
          print(f"now {name} is {age} years old")
    else:
        print("the dino does not exist")


'''
search by name 
at first add a dino in the zoo then search by name it should display the name and the age of that dino that you wrote 
'''
def searchByName():
    name = input("enter the name of the dino that you want to search about:")
    if name in dinosaur:
        print("Name:", name, "Age:", dinosaur[name])
    else:
        print("the dino that you wrote is not in the zoo")

while True:
    print("1.Add dinosaur")
    print("2.List all dinos in the zoo")
    print("3.delete dino by name")
    print("4.update dino's age")
    print("5.search by name")
    print("6.exit")
    choice = int(input("choose: "))
    if choice == 1:
        Adddino()
    elif choice == 2:
        listDinosaurs()
    elif choice == 3:
         deleteDino()
    elif choice == 4:
         updateDino()
    elif choice == 5:
        searchByName()
    elif choice == 6:
        break