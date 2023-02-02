

def triple_numbers(num):
    while True:
        num *= 3
        yield num

gen = triple_numbers(3)

for i in gen:
    if i > 100:
        gen.close()
    print(i)