
def myParse(char):
    try:
        f = int(char)
        return False
    except:
        return True


text = input("Введите своё имя: ")

result = False

for i in text:
    result = myParse(i)
    if result == False:
        print("Неправильный ввод!")
        break

print(f"В конечном итоге вот такой результат: {result}\n а строку получили такую {text}")



