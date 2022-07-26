# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PxmBqAe8DFAUq

import sys
sys.stdin = open("SW Expert Academy/220720/1986_input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    sum_ = 0
    
    for n in range(1, N + 1):
        if n % 2 != 0:
            sum_ += n
        else:
            sum_ -= n
    print(f'#{t} {sum_}')


