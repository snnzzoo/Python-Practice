# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2gbY0qAAQBBAS0

import sys
sys.stdin = open("SW Expert Academy/220719/1545_input.txt", "r")

N = int(input())
for n in range(N, -1, -1): # N부터 0까지 역순으로
    print(n, end=' ')