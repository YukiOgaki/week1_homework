import random

faces = int(input("サイコロの面の数は?: "))
times = int(input("何回振りますか?: "))


def dice(Face):
    return random.randint(1, Face)


x = 0
result = []

while x <= times - 1:
    result.append(dice(faces))
    x += 1
print(result)
