# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

# case 1.
numbers = [0, 20, 100]
max = numbers[0]
second = numbers[0]

for i in numbers:
    if max < i:
        second = max
        max = i
    elif second < i and i < max:
        second = i
print(second)

# case 2.
numbers = [0, 20, 100, 50, -60, 50, 100]
max = numbers[0]
second = numbers[0]

for i in numbers:
    if i > max:
        second = max
        max = i
    elif second < i and i < max:
        second = i
print(second)

# case 3.
numbers = [0, 1, 0]
max = float('-inf')
second = float('-inf')

for i in numbers:
    if i > max:
        second = max
        max = i
    elif second < i and i < max:
        second = i
print(second)

# case 4.
numbers = [-10, -100, -30]
max = numbers[0]
second = numbers[0]

for i in numbers:
    if i > max:
        second = max
        max = i
    elif second < i and i < max:
        second = i
print(second) # -10

numbers = [-10, -100, -30]
max_num = float('-inf')
second = float('-inf')

for i in numbers:
    if max_num < i:
        second = max_num
        max_num = i
    elif second < i and i < max_num:
        second = i
print(second) # -30