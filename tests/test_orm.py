import datetime

from src.orm import Database

db = Database()
test_data = {"name": "da!", "status": -1, "create_date": datetime.datetime.now()}
# db.add_task(**test_data)
# db.delete_task(test_data["create_date"])

print(db.load_tasks())
