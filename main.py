N = int(input("Введите число: "))

for i in range(N):
    if i % 2 == 0:
        continue
    else:
        print(f"{i}**5={i**5}")

