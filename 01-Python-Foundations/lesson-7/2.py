ID = []
with open("employees.txt", "r") as f:
    for txt in f.readlines():
        arr = txt.strip().split(", ")
        ID.append(arr[0])


class Employee:

    def __init__(self, Id, Name, Position, Salary):
        self.Id = Id
        self.Name = Name
        self.Position = Position
        self.Salary = Salary

    def __str__(self):
        return f"{self.Id}, {self.Name}, {self.Position}, {self.Salary}"

    def format(self):
        return f"{self.Id}, {self.Name}, {self.Position}, {self.Salary}\n"


class EmployeeManager:

    def Add(self):
        print("Enter your choice: 1")
        Id = input("Enter Employee ID: ")
        if Id in ID:
            print("Employee ID already exists")
            return
        Name = input("Enter Name: ")
        Position = input("Enter Position: ")
        try:
            Salary = float(input("Enter Salary: ").strip())
        except ValueError:
            print("Invalid salary. Must be a number.")
            return
        emp = Employee(Id, Name, Position, Salary)
        data = emp.format()
        with open("employees.txt", "a") as f:
            f.write(data)
        print("Employee added successfully!")
        ID.append(Id)

    def View(self):
        print("Enter your choice: 2")
        print("Employee Records:")
        with open("employees.txt", "r") as f:
            for txt in f.readlines():
                arr = txt.strip().split(", ")
                emp = Employee(arr[0], arr[1], arr[2], arr[3])
                print(emp)

    def Search(self):
        print("Enter your choice: 3")
        Id = input("Enter Employee ID to search: ")
        if Id not in ID:
            print("Employee ID does not exist")
            return

        with open("employees.txt", "r") as f:
            for txt in f.readlines():
                arr = txt.strip().split(", ")
                if arr[0] == Id:
                    emp = Employee(arr[0], arr[1], arr[2], arr[3])
                    print(emp)
                    return

    def Update(self):
        print("Enter your choice: 4")
        Id = input("Enter Employee ID to search: ")
        if Id not in ID:
            print("Employee ID does not exist")
            return

        data = ""
        with open("employees.txt", "r") as f:
            for txt in f.readlines():
                arr = txt.strip().split(", ")
                if arr[0] == Id:
                    Name = input("Enter Name: ")
                    Position = input("Enter Position: ")
                    try:
                        Salary = float(input("Enter Salary: ").strip())
                    except ValueError:
                        print("Invalid salary. Must be a number.")
                        return
                    emp = Employee(Id, Name, Position, Salary)
                    data += emp.format()
                else:
                    emp = Employee(arr[0], arr[1], arr[2], arr[3])
                    data += emp.format()
        with open("employees.txt", "w") as f:
            f.write(data)
        print("Employee updated!")

    def Delete(self):
        print("Enter your choice: 5")
        Id = input("Enter Employee ID to search: ")
        if Id not in ID:
            print("Employee ID does not exist")
            return

        data = ""
        with open("employees.txt", "r") as f:
            for txt in f.readlines():
                arr = txt.strip().split(", ")
                if arr[0] == Id:
                    continue
                emp = Employee(arr[0], arr[1], arr[2], arr[3])
                data += emp.format()
        with open("employees.txt", "w") as f:
            f.write(data)
        print("Employee deleted!")
        ID.remove(Id)

    def Exit(self):
        print("Goodbye!")
        exit()

    def menu(self):
        while True:
            print("Welcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choise = input()

            match choise:
                case "1":
                    self.Add()
                case "2":
                    self.View()
                case "3":
                    self.Search()
                case "4":
                    self.Update()
                case "5":
                    self.Delete()
                case "6":
                    self.Exit()
                case _:
                    print("Error")


manager = EmployeeManager()
manager.menu()
