import mypackage
import os

print(dir(mypackage))

mypackage.pyhton.hello(mypackage.test1)
print(mypackage.test.devigon(12, 6))
"""
file = open(r"mypackage\text.txt", encoding="utf-8")
text = file.read()
print(text)
file.close()
print(os.getcwd())
print(os.path.dirname(os.path.dirname("text.txt")))

with open(r"mypackage\text.txt", "a", encoding= "utf-8") as file:
    file.write("\nЯ заехал в отдельную комнату")

list1 = ["конь", "груша", "пианино"]
with open(r"mypackage\text.txt", "a", encoding= "utf-8") as file:
    file.write("\n" + " ".join(list1) + "\n")


with open(r"mypackage\text.txt" , "r", encoding= "utf-8") as file:
    for line in file:
        print(line.strip())
"""
a = "  Привет мир         "
a1 = "___ Вот так___"
a2 = "Привет \n это что"

print(a.strip(), a1.strip("_"), a2)



