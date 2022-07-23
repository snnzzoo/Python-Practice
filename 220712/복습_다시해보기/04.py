# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

# while 문
n = int(input())
result = 1
i = 1

while i <= n:
    result *= i
    i += 1
print(result)
# 1 <= 5
# result: 1 = 1*1 = 1
# i: 1 = 1 + 1 = 2
# 2 <= 5
# result: 1 = 1*2 = 2
# i: 2 = 2 + 1 = 3
# 3 <= 5
# result: 2 = 2*3 = 6
# i: 4
# 4 <= 5
# result: 6 = 6*4 = 24
# i: 5
# 5 <= 5
# result: 24 = 24*5 = 120


# for 문
n = int(input())
result = 1

for i in range(1, n+1):
    result *= i
print(result)
