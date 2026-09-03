import sys
import json
from pathlib import Path
from datetime import datetime

command = sys.argv[1]
file = Path("tasks.json")

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
        print("")
    case "delete":
        print("")
    case "mark-in-progress":
        print("")
    case "mark-done":
        print("")
    case "list":
        print("Listing all tasks")
    case "list-done":
        print("Listing done tasks")
    case "list-to-do":
        print("Listing to do tasks")
    case "list-in-progress":
        print("Listing in-progress tasks")

# print(sys.argv)