# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PhcWaAKIDFAUq

import sys
sys.stdin = open('SW Expert Academy/220720/1933_input.txt', 'r')

N = int(input())

# N을 어떤 수로 나누었을 때, 나머지(%)가 0이 나오면 N의 약수

for i in range(1, N + 1):
    if N%i == 0:
        print(i, end=' ')