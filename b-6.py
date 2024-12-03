import random

faces = int(input("サイコロの面の数は?: "))
times = int(input("何回振りますか?: "))


def dice(Face):
    return random.randint(1, Face)


result = []

for x in range(0, times):
    result.append(dice(faces))
    x += 1
print(result)
