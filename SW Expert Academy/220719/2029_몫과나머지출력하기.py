# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QGNvKAtEDFAUq

import sys
sys.stdin = open("SW Expert Academy/220719/2029_input.txt", "r")

t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'#{i} {a//b} {a%b}')
