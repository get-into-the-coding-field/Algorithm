'''
백준 11727. 2xn 타일링2
https://www.acmicpc.net/problem/11727
'''

n = int(input())
dp = [0, 1, 3]

for _ in range(3, n + 1):
    dp.append(dp[-1] + 2 * dp[-2])

print(dp[n] % 10007)