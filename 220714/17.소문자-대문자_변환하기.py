# 추가자료

word = 'banana'
result = ''

# 1
for char in word:
    # 1. 알파벳을 숫자로 바꾸고
    number = ord(char)
    # 2. 그 숫자에 -32를 하고
    number = number-32
    # 3. 다시 숫자를 알파벳으로 바꾼다.
    result += chr(number)
print(result)

# 2
for char in word:
    print(chr(ord(char)-32), end='')