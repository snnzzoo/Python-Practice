# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PhcWaAKIDFAUq

import sys
sys.stdin = open('SW Expert Academy/220720/1933_input.txt', 'r')

N = int(input())

# N % a == 0
# N을 a라는 수로 나눴을 때의 나머지가 0 : a는 N의 약수

for n in range(1, N + 1):
    if N % n == 0:
        print(n, end=' ')