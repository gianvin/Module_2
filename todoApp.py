import firebase_admin
from firebase_admin import credentials, firestore
import time
#Code for loading todoApp
cred = credentials.Certificate ("todoApp.json")

firebase_admin.initialize_app(cred)
db = firestore.client()

print("/ Firebase connected successfully")

#Code for adding the tasks
def add_tasks(date, thing_to_do, due, priority, category, remarks):
    task_ref = db.collection("tasks").add({
        "date": date,
        "thing_to_do": thing_to_do,
        "due": due,
        "priority": priority,
        "category": category,
        "remarks": remarks    
        })
    print("/ Tasks added successfully!")
# Function to list tasks
def list_tasks():
    try:
        tasks_ref = db.collection("tasks").stream()
        print("Current To-Do Tasks:")
        for task in tasks_ref:
            task_data = task.to_dict()
            print(f" -{task_data['date']} | {task_data['thing_to_do']} | Due: {task_data['due']} | "
              f"Priority: {task_data['priority']} | Category: {task_data['category']} | Remarks: {task_data['remarks']}")
    except Exception as e:
        print("x Error listing tasks:", e)
#Call the Function for adding tasks
if __name__ == "__main__":
    add_tasks(
        date = "2025-09-27",
        thing_to_do="Finish Writing the Code for Cloud Database",
        due="2025-09-28",
        priority="High",
        category="School",
        remarks="Done"
    )
    add_tasks(
        date="2025-09-27",
        thing_to_do="Record Video of my project",
        due="2025-09-28",
        priority="High",
        category="School",
        remarks="Will do"
    )

    add_tasks(
        date="2025-09-27",
        thing_to_do="Prepare documents for reimbursement of transportation expenses for the seminar attended",
        due="2025-10-03",
        priority="Least",
        category="Work",
        remarks="To do on Tuesday"
    )

    add_tasks(
        date="2025-09-27",
        thing_to_do="Encash Checks for Feeding Program sponsored by partner company",
        due="2025-09-30",
        priority="Medium",
        category="Work",
        remarks="To do on Tuesday"
    )
    add_tasks(
        date="2025-09-27",
        thing_to_do="Prepare lesson for Education for Better Work Class",
        due="2025-09-28",
        priority="High",
        category="Church",
        remarks="Done"
    )
    # List all tasks
    list_tasks()
       
# Code for reading tasks
def read_tasks():
    try:
        tasks = db.collection("tasks").stream()
        print("To-Do Tasks")
        for t in tasks:
            task = t.to_dict()
            print(f" -{task['date']} | {task['thing_to_do']} | Due: {task['due']} | "
              f"Priority: {task['priority']} | Category: {task['category']} | Remarks: {task['remarks']}")
    except Exception as e:
        print("X Error reading tasks:", e)

if __name__ == "__main__":
    read_tasks()

# Function to get specific tasks
def get_high_priority_tasks():
    try:
        tasks = db.collection("tasks").where("priority", "==", "High").stream()
        print("\n High Priority Tasks:")
        for task in tasks:
            data = task.to_dict()
            print(f" -{data['date']} | {data['thing_to_do']} | Due: {data['due']} | "
              f"Priority: {data['priority']} | Category: {data['category']} | Remarks: {data['remarks']}")
    except Exception as e:
        print("X Error reading  high priority tasks:", e) 
# function to take work tasks
def get_school_tasks():
    try:
        tasks = db.collection("tasks").where("category", "==", "School").stream()
        print("\n School Tasks:")
        for task in tasks:
            data_task = task.to_dict()
            print(f" -{data_task['date']} | {data_task['thing_to_do']} | Due: {data_task['due']} | "
              f"Priority: {data_task['priority']} | Category: {data_task['category']} | Remarks: {data_task['remarks']}")
    except Exception as e:
        print("X Error reading  school tasks:", e) 
#call Function  
if __name__ == "__main__":
    get_high_priority_tasks()
    get_school_tasks()
# function to receive notification when data on the cloud base changes
def on_snapshot(col_snapshot, changes, read_time):
    print("\ Firestore update detected!")
    for change in changes:
        if change.type.name == 'ADDED':
            print(f"+ New tasks added: {change.document.to_dict()}")
        elif change.type.name == 'MODIFIED':
            print(f" Task modified: {change.document.to_dict()}")
        elif change.type.name == 'REMOVED':
            print(f"X Task removed: {change.document.to_dict()}")
# Function Attach Listener
tasks_ref = db.collection("tasks")
query_watch = tasks_ref.on_snapshot(on_snapshot)

# Function to keep script running
print("Listening for changes...Press ctrl+C to exit.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped listening.")
