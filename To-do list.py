import tkinter as tk
from tkinter import messagebox
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks()
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✗"
        task_listbox.insert(tk.END, f"{status} {task['task']}")

def mark_completed():
    selected_index = task_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        tasks[index]["completed"] = not tasks[index]["completed"]
        save_tasks()
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task to mark complete!")

def delete_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        del tasks[index]
        save_tasks()
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")


tasks = load_tasks()


root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)
update_task_list()

complete_button = tk.Button(root, text="Mark Completed", command=mark_completed)
complete_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

root.mainloop()
