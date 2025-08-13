dinosaur = []
## ID, species, age
while True:
    print("1.Add dinosaur")
    print("2.exit")
    choice = int(input("choose: "))
    
    if choice == 1:
        dino_id = int(input("enter Id:"))
        species = int(input("enter species code:"))
        Age = int(input("enter the age: "))
        dinosaur.append([dino_id,species,Age])
        print(dinosaur)
    elif choice == 2:
        break