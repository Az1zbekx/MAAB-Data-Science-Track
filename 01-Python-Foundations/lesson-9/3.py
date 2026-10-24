import json
import csv
import os

tasks_file = "tasks.json"

if not os.path.exists(tasks_file):
    tasks = [
        {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
        {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
        {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
    ]
    with open(tasks_file, "w") as f:
        json.dump(tasks, f, indent=4)

with open(tasks_file, "r") as f:
    tasks = json.load(f)

for t in tasks:
    print(t["id"], t["task"], t["completed"], t["priority"])

total = len(tasks)
completed = sum(1 for t in tasks if t["completed"])
pending = total - completed
average_priority = round(sum(t["priority"] for t in tasks) / total, 1)

print("Total tasks:", total)
print("Completed tasks:", completed)
print("Pending tasks:", pending)
print("Average priority:", average_priority)

def modify_task(task_id, new_data):
    for t in tasks:
        if t["id"] == task_id:
            t.update(new_data)
            break
    with open(tasks_file, "w") as f:
        json.dump(tasks, f, indent=4)

def convert_to_csv(json_tasks, csv_file):
    with open(csv_file, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ID", "Task", "Completed", "Priority"])
        for t in json_tasks:
            w.writerow([t["id"], t["task"], t["completed"], t["priority"]])

convert_to_csv(tasks, "tasks.csv")
