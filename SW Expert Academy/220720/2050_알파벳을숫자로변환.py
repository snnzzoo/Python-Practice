# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QLGxKAzQDFAUq

import sys
sys.stdin = open("SW Expert Academy/220720/2050_input.txt", "r")

data = input()

# ord()는 특정 문자의 아스키코드 값으로 변환
# A는 65에 해당하므로 64를 빼 주면 된다.
for i in data:
    print(ord(i)-64, end=' ')
