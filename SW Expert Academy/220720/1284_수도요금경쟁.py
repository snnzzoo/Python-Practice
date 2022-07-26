# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV189xUaI8UCFAZN

import sys
sys.stdin = open("SW Expert Academy/220720/1284_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    
    # A사
    result_a = W * P
    # B사
    result_b = 0
    if W <= R:
        result_b = Q
    else:
        result_b = Q + (W - R) * S

    if result_a >= result_b:
        print(f'#{test_case} {result_b}')
    else:
        print(f'#{test_case} {result_a}')
