import os
import sys
import json
from datetime import datetime

if len(sys.argv) < 2:
    command = "help"
else:
    command = sys.argv[1]

commands = {
    "add": 1,
    "update": 2,
    "delete": 1,
    "mark-in-progress": 1,
    "mark-done": 1,
    "list": 0,
    "list-done": 0,
    "list-to-do": 0,
    "list-in-progress": 0,
    "help": 0
}

args = sys.argv[2:]

def parse_id(value):
    try:
        return int(value)
    except ValueError:
        return None

def load_tasks():
    if not os.path.exists("tasks.json"):
        return []

    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def find_task(tasks, id_num):
    for task in tasks:
        if task["id"] == id_num:
            return task

    return None

def find_task_index(tasks, id_num):
    for i, task in enumerate(tasks):
        if task["id"] == id_num:
            return i

    return None

def filter_tasks(tasks, status):
    filtered_tasks = []

    for task in tasks:
        if task["status"] == status:
            filtered_tasks.append(task)

    return filtered_tasks

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

def show_help():
    print("""
Task Tracker CLI

Usage:
    python test.py <command> [arguments]

Commands:
    add <description>              Add a new task
    update <id> <description>       Update a task
    delete <id>                     Delete a task
    mark-in-progress <id>           Mark a task as in progress
    mark-done <id>                  Mark a task as done
    list                            List all tasks
    list-done                       List completed tasks
    list-to-do                      List pending tasks
    list-in-progress                List tasks in progress
    """)

if command not in commands:
    print(f"Unknown command: {command}\n Run 'python test.py help' to see available commands")
    sys.exit()

if len(args) != commands[command]:
    print(f"Invalid arguments for command: {command}\nRun 'python test.py help' to see the correct syntax")
    sys.exit()

match command:
    case "add":
        tasks = load_tasks()
        
        new_id = 0
        found = False
        for i in range(len(tasks)):
            if i+1 != tasks[i]["id"]:
                new_id = i+1
                found = True
                break
        if not found:
            new_id = len(tasks) + 1

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_task = {
                    "id": new_id,
                    "description": args[0],
                    "status": "to-do",
                    "createdAt": current_time,
                    "updatedAt": "-"
                }

        tasks.insert(new_id-1, new_task)

        save_tasks(tasks)
        
    case "update":
        id_num = parse_id(args[0])

        if id_num is None:
            print("Task ID must be a number!")
        else:
            tasks = load_tasks()
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            task = find_task(tasks, id_num)

            if task:
                task["description"] = args[1]
                task["updatedAt"] = current_time
                save_tasks(tasks)
            else:
                print("There is no task with this ID.")
                    

    case "delete":
        id_num = parse_id(args[0])

        if id_num is None:
            print("Task ID must be a number!")
        else:
            tasks = load_tasks()

            i = find_task_index(tasks, id_num)

            if i is not None:
                tasks.pop(i)
                save_tasks(tasks)
            else:
                print("There is no task with this ID.")

    case "mark-in-progress":
        id_num = parse_id(args[0])

        if id_num is None:
            print("Task ID must be a number!")
        else:
            tasks = load_tasks()
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            task = find_task(tasks, id_num)

            if task:
                task["status"] = "in-progress"
                task["updatedAt"] = current_time
                save_tasks(tasks)
            else:
                print("There is no task with this ID.")

    case "mark-done":
        id_num = parse_id(args[0])

        if id_num is None:
            print("Task ID must be a number!")
        else:
            tasks = load_tasks()
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            task = find_task(tasks, id_num)
            
            if task:
                task["status"] = "done"
                task["updatedAt"] = current_time
                save_tasks(tasks)
            else:
                print("There is no task with this ID.")
    
    case "list":
        tasks = load_tasks()
        print_tasks(tasks)

    case "list-done":
        tasks = load_tasks()
        done_tasks = filter_tasks(tasks, "done")
        print_tasks(done_tasks)

    case "list-to-do":
        tasks = load_tasks()
        to_do_tasks = filter_tasks(tasks, "to-do")
        print_tasks(to_do_tasks)

    case "list-in-progress":
        tasks = load_tasks()
        in_progress_tasks = filter_tasks(tasks, "in-progress")
        print_tasks(in_progress_tasks)

    case "help":
        show_help()
