import sqlite3

FILE_NAME = "task.db"
TASKS_TABLE = "tasks"
ROW_NAMES = {"id": "tasks_id", "name": "name", "status": "status", "date": "date"}

connection = sqlite3.connect(FILE_NAME)
cursor = connection.cursor()


def read_row(task_name: str) -> dict:
    row_value = next(cursor.execute(f"SELECT * FROM {TASKS_TABLE} WHERE "
                                    f"{ROW_NAMES["name"]} LIKE \"{task_name}\";"))
    row_name = [description[0] for description in cursor.description]
    return {key: value for (key, value) in zip(row_name, row_value)}
    # std::cout << row;


if __name__ == '__main__':
    print(read_row("Задача1"))
