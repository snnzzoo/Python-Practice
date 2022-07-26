# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV189xUaI8UCFAZN

import sys
sys.stdin = open("SW Expert Academy/220720/1284_input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    a = W * P
    b = Q if W <= R else Q + (W - R) * S
    # if a < b:
        # print(f'#{t} {a}')
    # else:
        # print(f'#{t} {b}') # 실행시간: 0.13725s
    print(f'#{t} {min(a, b)}') # 실행시간: 0.13100s

