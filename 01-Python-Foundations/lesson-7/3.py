import json


class Task:
    def __init__(self, Title, Description, Due_Date, Status):
        self.Title = Title
        self.Description = Description
        self.Due_Date = Due_Date
        self.Status = Status

    def Dict(self):
        return {
            "title": self.Title,
            "decsription": self.Description,
            "due_data": self.Due_Date,
            "status": self.Status,
        }


class TaskManager:

    def __init__(self):
        self.tasks = {}
        self.Load()

    def Add(self):
        Id = input("Enter Task ID: ")
        if Id in self.tasks:
            print("Task ID already exists")
            return
        Title = input("Enter Title: ")
        Description = input("Enter Description: ")
        Due_Date = input("Enter Due Date (YYYY-MM-DD): ")
        Status = input("Enter Status (Pending/In Progress/Completed): ")
        task = Task(Title, Description, Due_Date, Status)
        self.tasks[Id] = task
        self.Save()
        print("Task added successfully!")

    def View(self):
        print("Enter your choice: 2")
        print("Tasks:")
        for Id, task in self.tasks.items():
            task = task.Dict()
            print(
                Id, task["title"], task["decsription"], task["due_data"], task["status"]
            )

    def Update(self):
        Id = input("Enter Task ID: ")
        if Id not in self.tasks:
            print("Task ID does not exist")
            return
        Title = input("Enter Title: ")
        Description = input("Enter Description: ")
        Due_Date = input("Enter Due Date (YYYY-MM-DD): ")
        Status = input("Enter Status (Pending/In Progress/Completed): ")
        task = Task(Title, Description, Due_Date, Status)
        self.tasks[Id] = task
        self.Save()
        print("Task updated successfully!")

    def Delete(self):
        Id = input("Enter Task ID: ")
        if Id not in self.tasks:
            print("Task ID does not exist")
            return
        self.tasks.pop(Id)
        self.Save()
        print("Task deleted successfully!")

    def Save(self):
        data = {Id: task.Dict() for Id, task in self.tasks.items()}
        with open("task.json", "w") as f:
            json.dump(data, f, indent=4)

    def Filter(self):
        Status = input("Enter Status to filter (Pending/In Progress/Completed): ")
        print(f"Tasks with status '{Status}':")
        for Id, task in self.tasks.items():
            if task.Status.lower() == Status.lower():
                t = task.Dict()
                print(Id, t["title"], t["description"], t["due_date"], t["status"])

    def Load(self):
        with open("task.json", "r") as f:
            data = json.load(f)
            for Id, d in data.items():
                task = Task(d["title"], d["decsription"], d["due_data"], d["status"])
                self.tasks[Id] = task

    def Exit(self):
        print("Goodbye!")
        exit()

    def manu(self):
        print("Welcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")

        choise = input()

        match choise:
            case "1":
                self.Add()
            case "2":
                self.View()
            case "3":
                self.Update()
            case "4":
                self.Delete()
            case "5":
                self.Filter()
            case "6":
                self.Save()
            case "7":
                self.Load()
            case "8":
                self.Exit()
            case _:
                print("Error")


Manager = TaskManager()
Manager.manu()
