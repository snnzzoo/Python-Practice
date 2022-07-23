# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

# 방법 1.
word = 'apple'
print(word[::-1])

# 방법 2.
word = 'banana'
result = ''
for i in word:
    result = i + result
print(result)

# 방법 3.
word = 'cherry'
print(''.join(reversed(word)))

# 방법 4.
word = 'kiwi'
for r in range(len(word)):
    # print(r)
    print(word[len(word)-r-1], end='')