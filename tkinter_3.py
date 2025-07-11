import tkinter as tk

def sum():
    rezult = 0
    numbers = entry.get().split()
    for number in numbers:
        number = int(number)
        rezult += number
    label.config(text=f"сумма равна: {rezult}")
    print(rezult)

root = tk.Tk()
root.title("Мой проектик")
root.geometry("400x400+100+100")
label = tk.Label(root, text="Введите текст через пробел")
label.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Найти сумму", command=sum)
button.pack()



root.mainloop()