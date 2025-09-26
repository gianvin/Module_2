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