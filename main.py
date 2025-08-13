dinosaur = []

def deleteDino():
    dinoid = int(input("which dino do you want to delete:"))
    for d in dinosaur:
        if d[0] == dinoid:
            dinosaur.remove(d)
        break

def Adddino():
        dino_id = int(input("enter Id:"))
        species = int(input("enter species code:"))
        Age = int(input("enter the age: "))
        dinosaur.append([dino_id,species,Age])

def listDinosaurs ():
    print(dinosaur)

while True:
    print("1.Add dinosaur")
    print("2.List all dinos in the zoo")
    print("3.delete dino by id")
    print("4.exit")
    choice = int(input("choose: "))
    if choice == 1:
        Adddino()
    elif choice == 2:
        listDinosaurs()
    elif choice == 3:
     deleteDino()
    elif choice == 4:
        break