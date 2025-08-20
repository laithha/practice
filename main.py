
grade = []

def deletegrade():
    score = int(input("enter the grade that you want to delete:"))
    if score in grade:
          grade.remove(score)
    else:
        print("the student is not in the database")

def addgrade():
        score = int(input("enter the grade"))
        grade.append(score)
        print(grade)

def listgrades ():
    if not grade:
            print("there is no scores in the database")
    print(grade)

def updatescore():
    score = int(input("what is the grade that you want to update: "))
    if score in grade:
          score1 = int(input("new grade:"))
          score2 = grade.index(score)
          grade[score2] = score1
    else:
        print("the student does not exist")

def searchByName():
    name = input("enter the name of the student that you want to search about")
    if name in grade:
        print("Name:", name, "grade:", grade[name])
    else:
        print("the student that you wrote is not in the database")


while True:
    print("WELCOME TO LAITH'S SCHOOL")
    print("1.Add score")
    print("2.List all score")
    print("3.delete score")
    print("4.update score ")
    print("5.search for a score")
    print("6.exit")
    choice = int(input("choose: "))
    if choice == 1:
        addgrade()
    elif choice == 2:
        listgrades()
    elif choice == 3:
         deletegrade()
    elif choice == 4:
         updatescore()
    elif choice == 5:
        searchByName()
    elif choice == 6:
        break