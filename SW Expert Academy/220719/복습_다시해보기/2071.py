# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QRnJqA5cDFAUq

import sys
sys.stdin = open('SW Expert Academy/220719/2071_input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    numbers = list(map(int, input().split()))
    sum_ = 0
    # print(numbers)
    for n in numbers:
        sum_ += n
    print(f'#{t} {round(sum_/len(numbers))}')
    # round() : 반올림 해주는 함수

