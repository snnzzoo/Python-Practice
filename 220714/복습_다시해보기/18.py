# 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

# 방법 1
word = 'banana'
result = {} # 딕셔너리

for i in word:
    # 딕셔너리에 key가 없으면
    if i not in result:
        # key와 값을 1로 초기화한다.
        result[i] = 1
    # 딕셔너리에 key가 있으면
    else:
        result[i] += 1
print(result)

# 방법 2
word = 'banana'
result = {}

for i in word:
    # result['a'] : 없으면 KeyError
    # result.get('a') : 없으면 기본값이 None
    # result.get('a', 0) : 없으면 기본값을 0으로 설정
    result[i] = result.get(i, 0) + 1
print(result)

# 출력 부분
for key in result:
    print(key, result[key])
