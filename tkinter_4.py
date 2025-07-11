import tkinter as tk
def add_task_listbox():
    task = entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        entry.delete(0, tk.END)

def del_selekt_task():
    task_selection = task_listBox.curselection()
    if task_selection:
        task_listBox.delete(task_selection)

def mark_task():
    task_selection = task_listBox.curselection()
    if task_selection:
        task_listBox.itemconfig(task_selection, bg="lightblue")

root = tk.Tk()
root.title("My_task")
root.geometry("400x400+100+100")
root.configure(background="hotpink")

label = tk.Label(root, text="Введите задачу")
label.pack(pady=5)

entry = tk.Entry(root, width=30, background="white")
entry.pack(pady=5)

add_task_button = tk.Button(root, text="Добавить задачу", width=20, background="LawnGreen", command=add_task_listbox)
delet_task_button = tk.Button(root, text="Удалить задачу", width=25, background="brown1", command=del_selekt_task)
mark_task_button = tk.Button(root, text="Пометить задание как выполненое", width=30, background="light sky blue", command=mark_task)

add_task_button.pack(pady=5)
delet_task_button.pack(pady=5)
mark_task_button.pack(pady=5)

label2 = tk.Label(root, text="Список моих задач")
label2.pack(pady=5)

task_listBox = tk.Listbox(root, height=10, width=50, background="lightpink")
task_listBox.pack(pady=5)

root.mainloop()