# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

# 방법 1
# case 1.
word = 'apple'
cnt = 0

for i in word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        cnt += 1
print(cnt)

# 방법 2
word = 'apple'
cnt = 0

for i in word:
    if i in 'aeiou':
        cnt += 1
print(cnt)

# 방법 3
word = 'apple'
cnt = 0

for i in word:
    if i == 'a':
        cnt += 1
    elif i == 'e':
        cnt += 1
    elif i == 'i':
        cnt += 1
    elif i == 'o':
        cnt += 1
    elif i == 'u':
        cnt += 1
print(cnt)

# case 2.
word = 'aeiou'
cnt = 0

for i in word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        cnt += 1
print(cnt)

# case 3.
word = 'zxcvb'
cnt = 0

for i in word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        cnt += 1
print(cnt)
