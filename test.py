import os
import sys
import json
from pathlib import Path
from datetime import datetime

command = sys.argv[1]
file = Path("tasks.json")

def load_tasks():
    if not os.path.exists("tasks.json"):
        return []

    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    return tasks

def print_tasks(tasks):
    if not tasks:
        print("No tasks found")
    else:
        headers = list(tasks[0].keys())

        col_widths = {}

        for key in headers:
            col_widths[key] = max(
            len(key),
            max(len(str(task[key])) for task in tasks)
            )

        format_str = "|".join([f"{{:<{col_widths[key]}}}" for key in headers])

        print(format_str.format(*headers))
        print("-+-".join(["-" * col_widths[key] for key in headers]))

        for row in tasks:
            print(format_str.format(*[str(row[key]) for key in headers]))

match command:
    case "add":
        if not file.exists():
            tasks = []
        else:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
        
        if len(sys.argv) < 3:
            print("Description is required")
        else:
            newID = 0
            found = False
            for i in range(len(tasks)):
                if i+1 != tasks[i]["id"]:
                    newID = i+1
                    found = True
                    break
            if not found:
                newID = len(tasks) + 1

            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            newTask = {
                        "id": newID,
                        "description": sys.argv[2],
                        "status": "to-do",
                        "createdAt": time,
                        "updatedAt": "-"
                    }

            tasks.append(newTask)

        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        
    case "update":
        if len(sys.argv) < 4:
            print("Task ID and description are required.")
        else:
            try:
                id_num = int(sys.argv[2])
            except ValueError:
                print("Task ID must be number!")
            else:
                tasks = load_tasks()
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                found = False
                if not tasks:
                    print("No tasks found!")
                else:
                    for i, task in enumerate(tasks):
                        if task["id"] == id_num:
                            task["description"] = sys.argv[3]
                            task["updatedAt"] = time
                            found = True
                            with open("tasks.json", "w") as file:
                                json.dump(tasks, file)
                                break

                    if not found:
                        print("There is no task with this ID.")

    case "delete":
        if len(sys.argv) < 3:
            print("Task ID is required")
        else:
            try:
                id_num = int(sys.argv[2])
            except ValueError:
                print("Task ID must be a number!")
            else:
                tasks = load_tasks()
                found = False
                if not tasks:
                    print("No tasks found!")
                else:
                    for i, task in enumerate(tasks):
                        if task["id"] == id_num:
                            tasks.pop(i)
                            found = True
                            with open("tasks.json", "w") as file:
                                json.dump(tasks, file)
                            break

                    if not found:
                        print("There is no task with this ID.")

    case "mark-in-progress":
        if len(sys.argv) < 3:
            print("Task ID is required.")
        else:
            try:
                id_num = int(sys.argv[2])
            except ValueError:
                print("Task ID must be number!")
            else:
                tasks = load_tasks()
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                found = False
                if not tasks:
                    print("No tasks found!")
                else:
                    for i, task in enumerate(tasks):
                        if task["id"] == id_num:
                            task["status"] = "in-progress"
                            task["updatedAt"] = time
                            found = True
                            with open("tasks.json", "w") as file:
                                json.dump(tasks, file)
                            break

                    if not found:
                        print("There is no task with this ID.")

    case "mark-done":
        if len(sys.argv) < 3:
            print("Task ID is required.")
        else:
            try:
                id_num = int(sys.argv[2])
            except ValueError:
                print("Task ID must be number!")
            else:
                tasks = load_tasks()
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                found = False
                if not tasks:
                    print("No tasks found!")
                else:
                    for i, task in enumerate(tasks):
                        if task["id"] == id_num:
                            task["status"] = "done"
                            task["updatedAt"] = time
                            found = True
                            with open("tasks.json", "w") as file:
                                json.dump(tasks, file)
                            break

                    if not found:
                        print("There is no task with this ID.")
    case "list":
        tasks = load_tasks()
        print_tasks(tasks)

    case "list-done":
        tasks = load_tasks()
        done_tasks = []

        for task in tasks:
            if task["status"] == "done":
                done_tasks.append(task)

        print_tasks(done_tasks)
    case "list-to-do":
        tasks = load_tasks()
        to_do_tasks = []

        for task in tasks:
            if task["status"] == "to-do":
                to_do_tasks.append(task)

        print_tasks(to_do_tasks)
    case "list-in-progress":
        tasks = load_tasks()
        in_progress_tasks = []

        for task in tasks:
            if task["status"] == "in-progress":
                in_progress_tasks.append(task)

        print_tasks(in_progress_tasks)

