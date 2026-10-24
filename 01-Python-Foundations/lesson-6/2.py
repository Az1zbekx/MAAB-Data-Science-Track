import random

ID = []
with open("employees.txt", "r") as f:
    for txt in f.readlines():
        arr = txt.strip().split(",")
        ID.append(arr[0])


def Add_new_employee_record():
    while True:
        x = str(random.randint(1, 10000))
        if x not in ID:
            emp_id = x
            break
    name = input("Name = ")
    position = input("Position = ")
    while True:
        try:
            salary = int(input("Salary = "))
            if salary < 0:
                print("Enter a positive number")
            else:
                break
        except ValueError as e:
            print(f"Error {e}")
    with open("employees.txt", "a") as f:
        txt = f"{emp_id},{name},{position},{salary}\n"
        f.write(txt)
    ID.append(emp_id)


def View_all_employee_records():
    with open("employees.txt", "r") as f:
        print(f.read())


def Search_for_an_employee_by_Employee_ID():
    emp_id = input("ID = ")
    if emp_id in ID:
        with open("employees.txt", "r") as f:
            for txt in f.readlines():
                arr = txt.strip().split(",")
                if arr[0] == emp_id:
                    print(f"{arr[1]}, {arr[2]}, {arr[3]}")
    else:
        print("There is no such ID")


def Update_an_employees_information():
    data = ""
    emp_id = input("ID = ")
    if emp_id in ID:
        with open("employees.txt", "r") as f:
            for txt in f.readlines():
                arr = txt.strip().split(",")
                if arr[0] == emp_id:
                    arr[1] = input("Name = ")
                    arr[2] = input("Position = ")
                    while True:
                        try:
                            salary = int(input("Salary = "))
                            if salary < 0:
                                print("Enter a positive number")
                            else:
                                arr[3] = str(salary)
                                break
                        except ValueError as e:
                            print(f"Error {e}")
                data += ",".join(arr) + "\n"
        with open("employees.txt", "w") as f:
            f.write(data)
    else:
        print("There is no such ID")


def Delete_an_employee_record():
    data = ""
    emp_id = input("ID = ")
    if emp_id in ID:
        with open("employees.txt", "r") as f:
            for txt in f.readlines():
                arr = txt.strip().split(",")
                if arr[0] == emp_id:
                    ID.remove(emp_id)
                    continue
                else:
                    data += ",".join(arr) + "\n"
        with open("employees.txt", "w") as f:
            f.write(data)
        print("Deleted successfully!")
    else:
        print("There is no such ID")


while True:
    print(
        "1. Add new employee record\n"
        "2. View all employee records\n"
        "3. Search for an employee by Employee ID\n"
        "4. Update an employee's information\n"
        "5. Delete an employee record\n"
        "6. Exit"
    )
    x = input()
    match x:
        case "1":
            Add_new_employee_record()
        case "2":
            View_all_employee_records()
        case "3":
            Search_for_an_employee_by_Employee_ID()
        case "4":
            Update_an_employees_information()
        case "5":
            Delete_an_employee_record()
        case "6":
            exit()
        case _:
            print("No clear key")
