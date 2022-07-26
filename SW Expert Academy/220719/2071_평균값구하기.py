# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QRnJqA5cDFAUq

import sys
sys.stdin = open('SW Expert Academy/220719/2071_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    sum = 0
    my_list = list(map(int, input().split()))
    for i in my_list:
        sum += i
    print(f'#{test_case} {round(sum/len(my_list))}')