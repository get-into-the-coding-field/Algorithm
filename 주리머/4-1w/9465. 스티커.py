'''
백준 9465. 스티커
https://www.acmicpc.net/problem/9465

2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
'''

'''
상하좌우,, X
그리고 대각선 X 아래 대각선 + 오른쪽이나 위 대각선 오른쪽 X
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    
    for i in range(1, n):
        if i == 1:
            sticker[0][i] += sticker[1][i-1]
            sticker[1][i] += sticker[0][i-1]
        else:
            sticker[0][i] = max(sticker[1][i-1], sticker[1][i-2]) + sticker[0][i]
            sticker[1][i] = max(sticker[0][i-1], sticker[0][i-2]) + sticker[1][i]
    print(max(sticker[0][n-1], sticker[1][n-1]))
