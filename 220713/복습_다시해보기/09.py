# 득표수 구하기

# print('이름을 입력하세요: ', end=' ')

# students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
# person = str(input())
# cnt = 0

# for i in students:
#     if i == person:
#         cnt += 1
# print(cnt)

# 이름을 잘못 입력한 경우
print('이름을 입력하세요: ', end=' ')

students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
person = str(input())
cnt = 0

for i in students:
    if i == person:
        cnt += 1
print(cnt)


