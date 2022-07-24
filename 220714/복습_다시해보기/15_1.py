# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지

# case 1.
word = 'HappyHacking'

for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx, end=' ')

# case 2.
word = 'banana'
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx, end=' ')

# case 3.
word = 'kiwi'
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx, end=' ')
