import tkinter as tk
import json
import os
from datetime import datetime
from time import strftime

CHECKMARKET = "\u2611"
BOX_EMPTY = "\u2610"
BG_COLOR = "#f0f0f0"

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
                               "completicion" : task_text.startswith(CHECKMARKET)})
                               
    with open("task.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

def load_task(sort_by_completion=True):
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
                tasks = data.get("tasks", [])
                if sort_by_completion:
                    tasks = sorted(tasks, key = lambda x : x["completicion"])
                task_listBox.delete(0, tk.END)
                for task in tasks:
                    task_listBox.insert(tk.END, task["text"])
                    status = task.get("completicion", [])
                    if status:
                        task_listBox.itemconfig(tk.END, bg="lightblue")
                    else:
                        task_listBox.itemconfig(tk.END, bg="white")        
                
        except FileNotFoundError:
            pass

        
def add_task_listBox():
    task = entry.get()
    if task:
        task = f"{BOX_EMPTY} {task}"
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
        if BOX_EMPTY in text:
            new_text = text.replace(BOX_EMPTY, CHECKMARKET)
        else:
            new_text = text.replace(CHECKMARKET, BOX_EMPTY)
        task_listBox.delete(i)
        task_listBox.insert(i, new_text)
        if BOX_EMPTY in text:
            task_listBox.itemconfig(i, bg = "lightblue")
        else:
            task_listBox.itemconfig(i, bg="white")
def refresh_listBox():
    save_task()
    task_listBox.delete(0, tk.END)
    tasks = load_task() 
    
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
btn_refrech = tk.Button(root, text="Обновить порядок", width=20, command=refresh_listBox)
btn_refrech.pack(pady=5)
task_listBox = tk.Listbox(root, selectmode="multiple", height=30, width=30)
task_listBox.pack(pady=5)
root.protocol("WM_DELETE_WINDOW", lambda : [save_task(), root.destroy()])
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(fill="both", expand=True, padx=10, pady=10)

print(task_listBox.get(0, tk.END))
load_task()
update_time()

# for index in selection:
#     print(task_listBox.get(index))
root.mainloop()
print(5)
