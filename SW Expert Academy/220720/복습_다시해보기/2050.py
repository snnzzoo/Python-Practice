# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QLGxKAzQDFAUq

import sys
sys.stdin = open("SW Expert Academy/220720/2050_input.txt", "r")

alphabet = input()

# ord()는 특정 문자를 아스키코드 값으로 변환해준다.
for a in alphabet:
    print(ord(a)-64, end=' ')
