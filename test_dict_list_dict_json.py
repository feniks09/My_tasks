import os
import json
# tasks = { 
#             "tasks" : [
#                 {"text" : "Привет", "finisd" : False},
#                 {"text" : "купаться", "finisd" : True}
#             ]
#     }
# tasks["tasks"].append({"text" : "Помыться", "finisd" : True})
# with open("dict_json.json", "w", encoding="utf-8") as file:
#     json.dump(tasks, file, ensure_ascii=False, indent=4)


with open("dict_json.json", "r", encoding="utf-8") as file:
    data = json.load(file)

    
    tasks = data["tasks"]
    print(tasks)
    # task_1 = tasks[0]
    # task_2 = tasks[1]
    # print(task_1["text"])
    # print(task_1["finisd"])
    # for index in range(len(tasks)):
    #    print(tasks[index]["text"])
    for task in tasks:
        print(f"{task["text"]} состояние - {task["finisd"]}")
    
    