## 1.
# a = input()
# print(a, type(a))

## 2-1.
# a = 8
# a //= 5
# print(a)

## 2-2.
# a = int(input())
# a //= 5
# print(a)

## 3.
# s = 'apple'
# print(s[::-1])

## 4.
# numbers = [3, 2, 1]
# sort_numbers = sorted(numbers)
# print(sort_numbers)

## 5.
# l = list([1, 2, 3])
# s = set([1, 2, 3])
# w = '123'
# t = tuple([1, 2, 3])

# print(l[0]) # 1
# print(s[0]) # TypeError: 'set' object is not subscriptable
# print(w[0]) # 1
# print(t[0]) # 1

## 6.
# print(list(map(int, '1234')))

## 7.
# a = 0
# while a <= 10:
#     a += 1
#     print(f'{a}', end=' ')

## 8.
# n = int(input())

# for i in range(3):
#     print('#', end='')

## 9.
# [4 1 11 10 2 8 6]
numbers = list(map(int, input().split()))
numbers.sort() # [1, 2, 4, 6, 8, 10, 11]
total = 0
count = 0
# print(len(numbers)) # 7
for i in range(1, len(numbers) - 1):
    # 1 2 3 4 5 6
    # 2 4 6 8 10 11
    total += numbers[i]
    # 0 = 0 + 2 = 2
    # 2 = 2 + 4 = 6
    # 6 = 6 + 6 = 12
    # 12 = 12 + 8 = 20
    # 20 = 20 + 10 = 30
    # 30 = 30 + 11 = 41
    # print(total)
    count += 1
    # 1 2 3 4 5 6
print(total // count)
# 2 3 4 5 6 

