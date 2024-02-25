import json


dataList=[]
# This loadData() method is used to load the data from json file before we perform the further operation
def loadData():
    global dataList 
    try:
        with open("Project/data.json",'r') as file:
            dataList=json.load(file)         
    except json.JSONDecodeError:
        dataList=[]

# Below function prints all the "ToDos" tasks
def getAllToDos():
    if len(dataList)!=0:
        enumerateList=enumerate(dataList)
        for i in enumerateList:
            id,data=i
            print(f"{id+1}. Title: {data.get("title")}")
            if data.get("Done"):
                print("Task Status: Done")
            else:
                print("Task Status: Pending")    
            print("*"*100)
    else:
        print("No task available.")        

# Below function gives the description of the "ToDo" Task
def get_description(input_id):
    enumerateList=enumerate(dataList)
    input_id_exists=False
    for i in enumerateList:
        id,data=i
        if(id+1)==input_id:
            input_id_exists=True
            print(f"{id+1}. Title: {data.get("title")}")
            print(f"Description: {data.get("description")}")
            if data.get("Done"):
                print("Task Status: Done")
            else:
                print("Task Status: Pending")    
            print("*"*10)
            break
    if not input_id_exists:
        print("Given ID doesn't exists!!!")

# Below function save the data in json file
def saveToDo():
    try:
        with open("Project/data.json",'w') as file:
            json.dump(dataList,file)
    except FileNotFoundError:
        print("ERROR: Unable to add")        

# Below function creates the "ToDo" task
def createToDo():
    title=input("Enter the title: ")
    description=input("Enter the description: ")
    data={"title":title,"description":description,"Done":False}
    dataList.append(data)
    saveToDo()

# Below function updates the data in "ToDo" task
def updateToDoList(input_id):
    enumerateList=enumerate(dataList)
    for i in enumerateList:
        id,data=i

        if(id+1)==input_id:
            print(data)
            response=input("Want to update title(Y/N)?")
            if(response=='Y' or response=='y'):
                new_title=input("Enter new title: ")
                data.update({"title":new_title})

            response=input("Want to update description(Y/N)?")
            if(response=='Y' or response=='y'):
                new_description=input("Enter new description: ")
                data.update({"description":new_description}) 
            print("Task updated successfully..",end="\n")    
            print(data) 
# Below function deletes the "ToDo" from the data
def deleteToDoList(input_id):
    if len(dataList)!=0:
        enumerateList=enumerate(dataList)
        for i in enumerateList:
            id,data=i
            if(id+1)==input_id:
                dataList.pop(id)
    else:
        print("No task is available.")

    saveToDo()

# Below function marks whether "ToDo" task is DONE or not
def  toDoIsDone(input_id):
    enumerateList=enumerate(dataList)
    for i in enumerateList:
        id,data=i
        if(id+1)==input_id:
            # print(data)
            response=input("Is task is done(Y/N)?")
            if(response=='Y' or response=='y'):
                data.update({"Done":True})

# Below function is main function which runs the whole program 
def main():
    loadData()
    while True:
        print("1. get all todos list\n2. get description of todolist\n3. Update todo list\n"
              +"4. Delete todo list\n5. create to do list \n6. todo done \n7. Exit")
        choice=input("enter the choice: ")
        print("*"*100)
        match choice:
            case "1": 
                   getAllToDos()
            case "2":
                id=input("Enter the id of task: ")
                get_description(int(id))
            case "3":
                id=input("Enter the id of task: ")
                updateToDoList(int(id))
            case "4":
                 id=input("Enter the id of task: ")
                 deleteToDoList(int(id))
            case "5":createToDo()
            case "6":
                id=input("Enter the id of task: ")
                toDoIsDone(int(id))
            case "7":break
            case _: choice=input("Invalid choice!! Try Again")


if __name__=="__main__":
    main()

        