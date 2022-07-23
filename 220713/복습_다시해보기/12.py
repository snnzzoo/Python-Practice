# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

word = 'apple'

# a가 아닐 경우 출력
for i in word:
    if i != 'a':
        print(i, end='')