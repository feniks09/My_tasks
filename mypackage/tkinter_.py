import tkinter as tk

root = tk.Tk()
# root2 = tk.Toplevel()
# root2.title("Мой второй проект")
# root2.geometry("400x400+100+500")
# root2.resizable(False, False)
root.title("Мой первый любимый проект")
root.geometry("400x400+100+100")
root.config(bg = "blue")
# label = tk.Label(root, text= "Мой очень красивый тест в красном цвете", fg= "red")
# label.pack()

# label2 = tk.Label(root, text = "Введите свое имя: ")
# label2.pack()
label3 = tk.Label(root, text = "Введите свое имя: ")
label3.grid(row=1, column=1)
# entry = tk.Entry(root)
# entry2 = tk.Entry(root)
# entry.pack()
# entry2.pack()
# def on_button_click():
#     label.config(text = "Кнопка была нажата")

#button = tk.Button(root, text= "Написать Привет мир!", command = lambda : label.config(text = "И тебе не хворать"))
# button2 = tk.Button(root, text= "Записать", command= lambda : label2.config(text= f"Ваше имя: {entry.get()}"))
# button2.pack()
button2 = tk.Button(root, text= "Мое имя", command= lambda : label3.config(text= "Алексей"))
button2.grid(row=1, column=2)


root.mainloop()
