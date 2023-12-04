import sqlite3


class Database:
    def __init__(self):
        self.db_name = "task.db"

    def add_task(self, task):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(f"""INSERT INTO tasks
        (name, status, start_date)
        VALUES (?, ?, ?");""", (task.name, task.status, task.start_date))
        connection.commit()
        cursor.close()
        connection.close()

    def update_task(self, task):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(f"""UPDATE tasks
        SET name = ?, status = ?, start_date = ?;""", (task.name, task.status, task.start_date))
        cursor.close()
        connection.close()

    def load_tasks(self, column_name="name", column_value="%"):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(f"""SELECT * FROM tasks
        WHERE ? LIKE ?;""", (column_name, column_value))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result


db = Database()
