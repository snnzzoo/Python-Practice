# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사용 금지

# case 1.
numbers = [0, 20, 100]
min = numbers[0]

for i in numbers:
    if min > i:
        min = i
print(min)

# case 2.
numbers = [0, 20, 100, 50, -60, 50, 100]
min = numbers[0]

for i in numbers:
    if min > i:
        min = i
print(min)

# case 3.
numbers = [0, 1, 0]
min = numbers[0]

for i in numbers:
    if min > i:
        min = i
print(min)

# case 4.
numbers = [-10, -100, -30]
min = numbers[0]

for i in numbers:
    if min > i:
        min = i
print(min)
