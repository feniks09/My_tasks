while True:
    input_user_info = input("Введите информацию: ")
    with open("mypackage/user_data.txt", "a+", encoding= "utf-8") as file:
        file.write(input_user_info + "\n")
        print(file.read())
