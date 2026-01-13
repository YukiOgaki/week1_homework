class Customer:
    # 各問のコードが期待通り動作するように実装
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        # C-6. 75歳以上の料金区分の追加
        if 0 <= self.age <= 3:
            return f"{0}"
        elif 3 < self.age < 20:
            return f"{1000}"
        elif 20 <= self.age < 65:
            return f"{1500}"
        elif 65 <= self.age < 75:
            return f"{1200}"
        elif 75 <= self.age:
            return f"{500}"
        else:
            return "0以上を入力してください"

    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    def info_align(self):
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"

    def info_grid(self):
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

# 以降で各問のコードを追加していく

print("C-1. フルネームを取得")
print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力

print("")
print("C-2. 年齢という概念の追加")
print(ken.age)  # 15 という値を出力
print(tom.age)  # 57 という値を出力
print(ieyasu.age)  # 73 という値を出力

print("")
print("C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる")
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力

print("")
print("C-4. 単一の顧客情報をCSV形式で取得できる")
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,73,1200" という値を出力

print("")
print("C-5. 3歳以下の入場料金の無料化")
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力
print(michelle.entry_fee())  # 0 という値を出力

print("")
print("C-6. 75歳以上の料金区分の追加")
print("     追加済み")

print("")
print("C-7. 単一顧客の情報取得形式の追加その1")
print(ken.info_align())  # "Ken Tanaka      15      1000" という値を出力
print(tom.info_align())  # "Tom Ford        57      1500" という値を出力
print(ieyasu.info_align())  # "Ieyasu Tokugawa 73      1200" という値を出力
print(michelle.info_align())  # "Michelle Tanner 3       0" という値を出力

print("")
print("C-8. 単一顧客の情報取得形式の追加その2")
print(ken.info_grid())  # "Ken Tanaka|15|1000" という値を出力
print(tom.info_grid())  # "Tom Ford|57|1500" という値を出力
print(ieyasu.info_grid())  # "IIeyasu Tokugawa|73|1200" という値を出力
print(michelle.info_grid())  # "Michelle Tanner|3|0" という値を出力
