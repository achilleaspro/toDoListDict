import datetime
import json
import os
import sys
import time
import operator

d = datetime

try:
    with open("toDoList.txt", 'r') as f:
        toDoDict = json.load(f)
except:
    toDoDict = {}

#Header
def header():
    print("#######################################")
    print("              TO DO LIST               ")
    print("#######################################")


#main Screen
def mainScreen():
    os.system('clear')
    header()
    print("---------------------------------------")
    print("              MAIN SCREEN              ")
    print("---------------------------------------")
    print("\n")
    print("Please choose one of the following options:\n")
    print("1. Add to the list")
    print("2. View the list")
    print("3. Mark as Completed")
    print("4. Delete from the list")
    print("5. Quit the program")
    print("\n")
    choice = input("Please enter the number of your choice: ")
    print("----- Press ENTER to return to main screen -----")
    if len(choice) > 0:
        if choice.lower()[0] == "1":
            addScreen()
        elif choice.lower()[0] == "2":
            viewScreen()
        elif choice.lower()[0] == "3":
            completedList()
        elif choice.lower()[0] == "4":
            deleteScreen()
        elif choice.lower()[0] == "5":
            with open("toDoList.txt", "w") as fo:
                fo.write(json.dumps(toDoDict))
            print("Dictionary: ", toDoDict)
            sys.exit()
        else:
            print("Wrong Value Entered: Please Try Again.")
            time.sleep(1.5)
            mainScreen()
    else:
        mainScreen()

# addScreen
def addScreen():
    os.system('clear')
    header()
    print("---------------------------------------")
    print("                ADD ITEM               ")
    print("---------------------------------------")
    print("\n\n")
    print("Please enter the name of the item that you want to add.")
    print("----- Press ENTER to return to main screen -----")
    item = input("\nItem: ")
    if len(item) == 0:
        mainScreen()
    date = input("Date (m/d/y): ")
    if len(item) > 0 and len(date) > 0:
        toDoDict[item] = [date, 'PENDING']
        for key, value in toDoDict.items():
            print(key, " : ", value)
        print("Item added...")
        time.sleep(2)
        mainScreen()
    else:
        mainScreen()

# viewScreen
def viewScreen():
    os.system('clear')
    header()
    print("---------------------------------------")
    print("               VIEW SCREEN             ")
    print("---------------------------------------")
    print("\n")
    newDict = dict(sorted(toDoDict.items(), key=lambda x: x[1][1], reverse=True))
    for key, value in newDict.items():
        overdue = ''
        if datetime.datetime.strptime(value[0], "%m/%d/%Y").date() < datetime.datetime.today().date():
            overdue = '*OVERDUE*'
        #if value[1] == "COMPLETED":
        print("##### Task: ", key, " #####\n" "DueDate: ", value[0], "\n" "State is: ", value[1], overdue, "\n\n")

    print("\n")
    print("Press enter to return to the main menu")
    input()
    mainScreen()

#completedlist
def completedList():
    os.system('clear')
    header()
    print("---------------------------------------")
    print("         ALTER STATE ITEM              ")
    print("---------------------------------------")
    for key, value in toDoDict.items():
        print(key, " : ", value)
    print("\nWhich task to `update state?")
    choice = input("Task Name: ")
    try:
        if len(choice) > 0:
            toDoDict[choice][1] = 'COMPLETED'
            print(toDoDict)
            time.sleep(2)
    except:
        print("Invalid Task Name.")
        time.sleep(1)
        completedList()
        mainScreen()
    else:
        mainScreen()

# deleteScreen
def deleteScreen():
    os.system('clear')
    header()
    print("---------------------------------------")
    print("              DELETE ITEM              ")
    print("---------------------------------------")
    for key, value in toDoDict.items():
        print(key, " : ", value)
    print("\nWhich task to delete?")
    choice = input("Task Name: ")
    try:
        if len(choice) > 0:
            toDoDict.pop(choice)
            print(toDoDict)
            time.sleep(2)
    except:
        print("Invalid Task Name.")
        time.sleep(1)
        deleteScreen()
        mainScreen()
    else:
        mainScreen()



mainScreen()