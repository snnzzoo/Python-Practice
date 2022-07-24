# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

# number = 123
# 123 = 1 x 100 + 2 x 10 + 3 x 1
number = int(input())
cnt = 0

while number > 0:
    number //= 10
    cnt += 1
print(cnt)

# str() 사용
number = 123

if number <= 0:
    print('양의 정수를 입력하세요.')
else:
    print(len(str(number)))