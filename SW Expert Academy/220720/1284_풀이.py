# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV189xUaI8UCFAZN

import sys
sys.stdin = open('SW Expert Academy/220720/1284_input.txt', 'r')

# A사 : 1L * P원
# B사 :
#  R 이하 : Q
#  R 초과 : Q + S*(W-R)

T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    # print(P, Q, R, S, W)
    A = W * P
    # if R > W:
    #     B = Q
    # else:
    #     B = Q + S*(W-R)
    B = Q if R > W else Q + S*(W-R)    

    print(f'#{test_case} {min(A, B)}')
