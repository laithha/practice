dinosaur = []
def listDinosaurs ():
    print(dinosaur)
while True:
    print("1.Add dinosaur")
    print("2.List all dinos in the zoo")
    print("3.exit")
    choice = int(input("choose: "))
    
    if choice == 1:
        dino_id = int(input("enter Id:"))
        species = int(input("enter species code:"))
        Age = int(input("enter the age: "))
        dinosaur.append([dino_id,species,Age])
    elif choice == 2:
        listDinosaurs()
    elif choice == 3:
        break