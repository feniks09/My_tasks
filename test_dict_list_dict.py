task = "Рыжики"
task2 = "доступ без ключа"
task3 = "яхтиг в этом году"
tasks = {
            "tasks" : [
                {"text" : task, "complect" : True},
                {"text" : task2, "complect" : True}
            ]
        }
# print(tasks)
# print(tasks["tasks"])
# for task in tasks["tasks"]:
#     print(task)
# print(tasks['tasks'])
# for task in tasks["tasks"]:
#     text = task["text"]
#     complect = task["complect"]
#     print(text, "- Состояние задачи: ", complect)
# print(tasks["tasks"][0])
tasks["tasks"].append({"text" : task3, "complect" : True})
# tasks1 = tasks["tasks"]
# tasks["tasks"][0]["text"] = "Все Ок"
# tasks["tasks"][0]['complect'] = True
# print(tasks["tasks"])
# a = [print(key, "-", value) for key, value in tasks["tasks"].items()]
for index, task in enumerate(tasks["tasks"]):
    status = "Ok" if task["complect"] == True else "No"
    print(f"{index}. [{status}] - {task["text"]}")
