import tkinter as tk
root = tk.Tk()
root.title("Это мой второй любимый проект")
root.geometry("400x400+100+100")
label = tk.Label(root, text="Введите числа через пробел")
label.pack()
def sum():
    nambers = entry.get().split()
    rezult = 0
    for namber in nambers:
        namber = int(namber)
        rezult += namber
    label.config(text=f"Cумма чисел: {rezult}")
    print(rezult)  
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Сложить числа", command=sum)
button.pack()




root.mainloop()