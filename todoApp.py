import firebase_admin
from firebase_admin import credentials, firestore

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
# Code for reading tasks
def get_tasks():
    tasks = db.collection("tasks").stream()
    print("\n To-Do List")
    for task in tasks:
        data = task.to_dict()
        print(f" -{data['date']} | {data['thing_to_do']} | Due: {data['due']} | "
              f"Priority: {data['priority']} | Category: {data['category']} | Reamrks: {data['remarks']}")