rows = int(input("行数を入力してください: "))
columns = int(input("列数を入力してください: "))

for row in range(1, rows + 1):
    for column in range(1, columns + 1):
        print(row * column, end=" ")
    print()
