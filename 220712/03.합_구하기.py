# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# sum() 함수 사용 금지

# while 문

# 값 초기화 (처음 시작 값)
n = 0
# 0부터 더하기 위해서
result = 0
# user_input 값
user_input = int(input())

# 방법 1
while n <= user_input:
    result += n
    n += 1
print(result)

# 방법 2
while n < user_input:
    print(f'n: {n}, result: {result}') # 그때마다의 결과 적어 놓으면 디버깅 시 편리함
    n += 1
    result += n
print(result)
