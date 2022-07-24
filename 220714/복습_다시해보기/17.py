# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지

# 방법 1
word = 'banana'

for i in word:
    # 문자를 숫자로 print(ord(i))
    print(chr(ord(i)-32), end='')

print('\n')
# 방법 2
word = 'banana'
result=''

for i in word:
    # 문자를 숫자로
    number = ord(i)
    # print(number)
    result = number - 32
    # print(result)
    # 숫자를 문자로
    print(chr(result), end='')

print('\n')
# 방법 3
word = 'banana'
print(word.upper())

# 방법 4
word = 'banana'
print(word.swapcase())