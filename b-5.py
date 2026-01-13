str_input = input("データを入力してください(スペース区切り) > ")
str_nums = str_input.split()

nums = []
x = 0

while x <= len(str_nums) - 1:
    nums.append(int(str_nums[x]))
    x += 1


# 1、合計値
def total_pt(Nams):
    total = 0

    for num in Nams:
        total += num
    return total


# 2、最大値
def max_pt(Nams):
    maximum = max(Nams)
    return maximum


# 3、最小値
def min_pt(Nams):
    miniimum = min(Nams)
    return miniimum


# 4、平均値
def avg_pt(Nams):
    total = total_pt(Nams)
    lens = len(str_nums)
    average = total / lens
    return int(average)


print(f"合計値: {total_pt(nums)}")
print(f"最大値: {max_pt(nums)}")
print(f"最小値: {min_pt(nums)}")
print(f"平均値: {avg_pt(nums)}")
