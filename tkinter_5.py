import tkinter as tk
import json
import os
from datetime import datetime
from time import strftime

data = {"время": datetime.now}
def datatime_handler(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("несериализируемый объект")
#print(datatime_handler(data))

def update_time():
    current_time = strftime("%H:%M:%S")
    time_libel.config(text=current_time)
    time_libel.after(1000, update_time)
#print(current_time)
 
def save_task():
    tasks = {"tasks" : []}
    for i in range(task_listBox.size()):
        task_text = task_listBox.get(i)
        tasks["tasks"].append({"text" : task_text, 
                               "completicion" : task_text.startswith(checkmark)})
    with open("task.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

checkmark = "\u2611"
box_empty = "\u2610"

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
                data = json.load(file)
                task_listBox.delete(0, tk.END)
                for task in data["tasks"]:
                    task_listBox.insert(tk.END, task["text"])
                    status = task["completicion"]
                    if status:
                        task_listBox.itemconfig(tk.END, bg="lightblue")
                    else:
                        task_listBox.itemconfig(tk.END, bg="white")
                
        except FileNotFoundError:
            pass

        
def add_task_listBox():
    task = entry.get()
    if task:
        task = f"{box_empty} {task}"
        task_listBox.insert(tk.END, task)
        entry.delete(0, tk.END)
    
def del_task_listBox():
    selection = list(task_listBox.curselection())
    print(selection)
    text = task_listBox.get(0, tk.END)
    for i in sorted(selection, reverse=True):
        i = int(i)
        task_listBox.delete(i)
        text1 = task_listBox.get(i)
        print(f"{text1} : {i}")


def mark_and_no_mark_task_listBox():
    selection = task_listBox.curselection()
    print(selection)
    for i in selection:
        i = int(i)
        text = task_listBox.get(i)
        print(text)
        if box_empty in text:
            new_text = text.replace(box_empty, checkmark)
        else:
            new_text = text.replace(checkmark, box_empty)
        task_listBox.delete(i)
        task_listBox.insert(i, new_text)
        if box_empty in text:
            task_listBox.itemconfig(i, bg = "lightblue")
        else:
            task_listBox.itemconfig(i, bg="white")
  
    
root = tk.Tk()
root.title("Мои задачи")
root.geometry("400x400+100+100")
root.configure(background = "Hotpink")

time_libel = tk.Label(root, width=8, bg="white", fg="black")
time_libel.pack(padx=20, pady=20)

entry = tk.Entry(root, width=50, background="white")
entry.pack(pady=5)

label = tk.Label(root, width=30, background="Hotpink")
label.pack(pady=5)
label.config(text="Введите вашу задачу")

add_task_button = tk.Button(root, text="Добавить задачу", width=30, background="green", command=add_task_listBox)
add_task_button.pack(pady=5)

del_task_button = tk.Button(root, text="Удалить задачу", width=25, background="red", command=del_task_listBox)
del_task_button.pack(pady=5)

# mark_task_button = tk.Button(root, text="Пометить задачу как выполненную", width=30, background="blue", command=mark_task_listBox)
# mark_task_button.pack(pady=5)

# no_mark_task_button = tk.Button(root, text="Снять пометку", width=25, background="white", command=no_mark_task_listBox)
# no_mark_task_button.pack(pady=5)
mark_NO_mark_task_button = tk.Button(root, text="Пометить или снять пометку", width=30, background="yellow", command=mark_and_no_mark_task_listBox)
mark_NO_mark_task_button.pack(pady=5)

task_listBox = tk.Listbox(root, selectmode="multiple", height=30, width=30)
task_listBox.pack(pady=5)
root.protocol("WM_DELETE_WINDOW", lambda : [save_task(), root.destroy()])
print(task_listBox.get(0, tk.END))
load_task()
update_time()

# for index in selection:
#     print(task_listBox.get(index))
root.mainloop()

