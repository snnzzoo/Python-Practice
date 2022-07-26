# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QGNvKAtEDFAUq

import sys
sys.stdin = open("SW Expert Academy/220719/2029_input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'#{t} {a // b} {a % b}')
