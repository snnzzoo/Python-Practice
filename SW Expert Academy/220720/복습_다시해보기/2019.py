# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QDEX6AqwDFAUq

import sys
sys.stdin = open("SW Expert Academy/220720/2019_input.txt", "r")

N = int(input())

for n in range(0, N + 1):
    result = 2 ** n
    print(result, end=' ')