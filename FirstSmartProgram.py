def my_parse(char):
    try:
        f = int(char)
        return False
    except:
        return True


def my_input(string, checker):
    result = False
    text = input(string)
    for char in text:
        result = my_parse(char)
        if result != checker:
            break
    return text, result


def greetings(name, age):
    if age == "":
        age = "Не указан"
    print(f"Добро пожаловать {name}, Возраст: {age}")


def main():
    while True:
        result = False
        age = None
        name, result = my_input("Введите своё имя: ", True)

        if not result:
            print("Неправильный ввод имени!")
            continue

        age, result = my_input("Введите свой возраст: ", False)

        if result:
            print("Неправильный ввод возраста!\n")
            continue

        greetings(name=name, age=age)
        break


main()
