import json
list1 = "Hello word"
with open("list1.json", "w", encoding="utf-8") as f:
    json.dump(list1, f, ensure_ascii=False, indent=4)