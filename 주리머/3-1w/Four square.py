'''
백준 17626. Four squares
https://www.acmicpc.net/problem/17626
'''

import sys 
input = sys.stdin.readline
n = int(input())
dp = [0, 1]
# 4개 이하 제곱 수

count = 0
for i in range(int(n**0.5), 0, -1):
    dp[n] += dp[i]

print(dp[n])

3 