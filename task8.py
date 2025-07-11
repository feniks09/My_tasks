import tkinter as tk
import json
import os
from datetime import datetime
data = {"время": datetime.now}
def datatime_handler(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("несериализируемый объект")
#print(datatime_handler(data))

def save_task():
    task = task_listBox.get(0, tk.END)
    with open("task.json", "w", encoding="utf-8") as file:
        json.dump(task, file, ensure_ascii=False, indent=4)


def load_task():
    if not os.path.exists("task.json"):
        with open("task.json", "w", encoding="utf-8") as file:
            json.dump([], file) 
        return
    with open("task.json", "r", encoding="utf-8") as file:
        task = file.read().strip()
        if not task:
            with open("task.json", "w", encoding="utf-8") as file:
                json.dump([], file)
            return
        try:

            with open("task.json", "r", encoding="utf-8") as file:
                tasks = json.load(file)
                for task in tasks:
                    task_listBox.insert(tk.END, task)
        except FileNotFoundError:
            pass


        
def add_task_listBox():
    task = entry.get()
    if task:
        task_listBox.insert(tk.END, f"[] {task}")
        entry.delete(0, tk.END)

def del_task_listBox():
    selection = task_listBox.curselection()
    if selection:
        task_listBox.delete(selection)

def mark_and_no_mark_task_listBox():
    selection = task_listBox.curselection()
    index = selection[0]
    text = task_listBox.get(index)
    if "[]" in text:
        new_text = text.replace("[]", "[X]")    
    else:
        new_text = text.replace("[X]", "[]")    
    task_listBox.delete(index)
    task_listBox.insert(index, new_text)
    if "[]" in text:
        task_listBox.itemconfig(index, bg = "lightblue")
    else:
        task_listBox.itemconfig(index, bg="whte")
    
    


def mark_task_listBox():
    global selection
    selection = task_listBox.curselection()
    if selection:
        task_listBox.itemconfig(selection, background="blue")
def no_mark_task_listBox():
    selection = task_listBox.curselection()
    if selection:
        task_listBox.itemconfig(selection, background="white")
root = tk.Tk()
root.title("Мои задачи")
root.geometry("400x400+100+100")
root.configure(background = "Hotpink")

label = tk.Label(root, text="Введите вашу задачу", width=30, background="Hotpink2")
label.pack(pady=5)

entry = tk.Entry(root, width=50, background="white")
entry.pack(pady=5)

add_task_button = tk.Button(root, text="Добавить задачу", width=30, background="green", command=add_task_listBox)
add_task_button.pack(pady=5)

del_task_button = tk.Button(root, text="Удалить задачу", width=25, background="red", command=del_task_listBox)
del_task_button.pack(pady=5)

mark_task_button = tk.Button(root, text="Пометить задачу как выполненную", width=30, background="blue", command=mark_task_listBox)
mark_task_button.pack(pady=5)

no_mark_task_button = tk.Button(root, text="Снять пометку", width=25, background="white", command=no_mark_task_listBox)
no_mark_task_button.pack(pady=5)
mark_NO_mark_task_button = tk.Button(root, text="Пометить или снять пометку", width=30, background="yellow", command=mark_and_no_mark_task_listBox)
mark_NO_mark_task_button.pack(pady=5)

task_listBox = tk.Listbox(root, height=30, width=30)
task_listBox.pack(pady=5)
root.protocol("WM_DELETE_WINDOW", lambda : [save_task(), root.destroy()])
print(task_listBox.get(0, tk.END))
load_task()

# for index in selection:
#     print(task_listBox.get(index))
root.mainloop()



