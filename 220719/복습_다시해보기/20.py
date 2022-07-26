# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요.

number = int(input())
answer = 0

while number:
    answer += number % 10
    number //= 10
print(answer)

# divmod(a, b)
# a를 b로 나누고, 그 결과를 tuple로 반환해준다. (몫, 나머지)
number = int(input())
answer = 0

while number:
    number, remainder = divmod(number, 10)
    answer += remainder
print(answer)