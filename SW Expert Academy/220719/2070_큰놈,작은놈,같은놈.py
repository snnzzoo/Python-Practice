# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QQ6qqA40DFAUq

import sys
sys.stdin = open('SW Expert Academy/220719/2070_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    if a < b:
        print(f'#{test_case} <')
    elif a > b:
        print(f'#{test_case} >')
    else:
        print(f'#{test_case} =')
