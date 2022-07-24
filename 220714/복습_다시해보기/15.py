# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

# case 1.
word = 'banana'

# word의 길이만큼 반복
# range(len(word)) => range(0, 6) => 0, 1, 2, 3, 4, 5
for idx in range(len(word)):
    # print(idx, word[idx])
    if word[idx] == 'a':
        print(idx)
        # a가 최초 등장 후 stop
        break
else:
    print(-1)

# case 2.
word = 'apple'

for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        break
else:
    print(-1)

# case 3.
word = 'kiwi'

for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        break
else:
    print(-1)


## 메서드 사용
word = 'coffee'

print(word.find('f'))
print(word.index('f'))

print(word.find('a')) # 없는 경우 -1 반환
print(word.index('a')) # 없는 경우 ValueError
