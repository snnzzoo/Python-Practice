# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

# case 1.
numbers = [0, 20, 100]
max = numbers[0]

for i in numbers:
    if max <= i:
        max = i
print(max)

# case 2.
numbers = [0, 20, 100, 50, -60, 50, 100]
max = float('-inf')

for i in numbers:
    if max <= i:
        max = i
print(max)

# case 3.
numbers = [0, 1, 0]
max = numbers[0]

for i in numbers:
    if max <= i:
        max = i
print(max)

# case 4.
numbers = [-10, -100, -30]
max = numbers[0]

for i in numbers:
    if max < i:
        max = i
print(max)