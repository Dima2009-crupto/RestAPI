from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Ініціалізація бази даних
def init_db():
    with sqlite3.connect("tasks.db") as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL
        )
        """)
init_db()

# Головна сторінка
@app.route('/')
def index():
    return render_template("index.html")

# Отримати список завдань
@app.route('/tasks', methods=['GET'])
def get_tasks():
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.execute("SELECT id, description FROM tasks")
        tasks = [{"id": row[0], "description": row[1]} for row in cursor.fetchall()]
    return jsonify(tasks)

# Додати нове завдання
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    description = data.get('description')
    with sqlite3.connect("tasks.db") as conn:
        conn.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
    return jsonify({"message": "Task added successfully"}), 201

# Видалити завдання
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    with sqlite3.connect("tasks.db") as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    return jsonify({"message": "Task deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)

