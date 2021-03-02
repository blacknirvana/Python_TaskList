#Python task list example

taskList = []

def commander():
    print("\na to add, s to show list, q to quit")
    commandOrder = input("Command --> ")
    
    if commandOrder == "a":
        addTasks()
    if commandOrder == "s":
        printTasklist()
    if commandOrder == "q":
        print("Bye Bye Friend....")
        
def addTasks():
    print("Please enter a task (Q to stop adding):")
    while True:
        newTask = input("Task --> ")
        if str.lower(newTask) == "q":
            commander()
        taskList.append(newTask)


def printTasklist():
    print("\n\nTasklist:")
    print("----------------------------")
    taskCounter = 0    
    for task in taskList:
        taskCounter += 1
        print(f"#{taskCounter} {task.title()}")
    commander()
#program starts running here

print("Python Tasklist v 1.0\n")

commander()