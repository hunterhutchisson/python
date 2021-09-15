import pickle

#to add task function
def addtask(priority, task):
    todolist[priority].append(task)
    print()

#to delete task function
def todeletetask(deletedtask):
    for task_list in todolist.values():
        if deletedtask in task_list:
            task_list.remove(deletedtask)
    print()

#to view list of tasks function
def viewall():
    tasklst = []
    j = 0
    for priority in todolist.keys():
        for individualtask in todolist[priority]:
            tasklst.append(individualtask)
            print(f"{j+1} - {individualtask} - {priority}")
            j += 1
    print()
    return tasklst

#empty priority lists
high= []         
medium = []    
low = []         

#starting todo list
todolist = {"high" : high, "medium" : medium, "low" : low}

# needed for initial file creating then comment out after first use.
with open("todolist.pickle", "wb") as fh:
    pickle.dump(todolist, fh)

with open("todolist.pickle", "rb") as fh:
    todolist = pickle.load(fh)

while True:
    val = input("""Press 1 to add task
Press 2 to delete task
Press 3 to view all tasks
Press q to quit
""")
    print()
    if val == "1":
        while True:
            task = input("What task would you like to add: ")
            priority = input("What level of priority is the task? high, medium, or low: ")
            if (len(task) > 0) and (priority == "high" or priority == "medium" or priority == "low"):
                addtask(priority, task)
                break
            else:
                print("Not a valid input. No tasks were added.\n")
                break
    elif val == "2":
        while True:
            tasklst = viewall()
            deletedindex = int(input("What number do you want to delete? "))-1
            if (deletedindex >= 0) and (deletedindex < len(tasklst)):
                deletedtask = tasklst[deletedindex]
                todeletetask(deletedtask)
                break
            else:
                print("That number wasn't on the list. No tasks were deleted.\n")
                break
    elif val == "3":
        viewall()
    elif val =="q":
        break
    else:
        print("Not a valid input.\n")

with open("todolist.pickle", "wb") as fh:
    pickle.dump(todolist, fh)