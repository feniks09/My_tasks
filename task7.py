import tkinter as tk

def name():
    name = entry.get()
    label.config(text= f"Привет, {name} !!!")

root = tk.Tk()
root.title("Приветствие пользователя")
root.geometry("400x400+100+100")
label = tk.Label(root, text="Для входа введите свое имя")
label.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Вход", command=name)
button.pack()

root.mainloop()