toDoList = ["Einkaufen","Schwimmen","Lernen","Basketball"]
def addTask(task):
    toDoList.append(task)

def removeTask(taskToRemove):
    global toDoList
    print(type(taskToRemove))
    if isinstance(taskToRemove, str): #if taskToRemove is a string, we can do a list comprehension
        #          [expression for item in iterable if condition]          !!!!!!!LIST COMPREHENSION!!!!!!!!
        toDoList = [task for task in toDoList if task != taskToRemove]
    elif isinstance(taskToRemove, int): # if taskToRemove is an int, we want to delete it by index
        if 0 <= taskToRemove < len(toDoList):
            print(f"removing {toDoList[taskToRemove]} from todoList")
            toDoList.pop(taskToRemove)
        else:
            print("index not found!")  # if number wasnt an index of todoList

    else:
        print("dont hack me, just use string or number.")

removeTask(1)
def showTasks():
    global toDoList
    print("to-do list:")
    for task in toDoList:
        print(task)



