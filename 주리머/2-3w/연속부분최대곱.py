'''
연속부분최대곱
https://www.acmicpc.net/problem/2670
'''

n = int(input())
arr = [float(input()) for _ in range(n)]
dp = [0] * n
maxVal = arr[0]

for i in range(n):
    dp[i] = max(arr[i], dp[i-1] * arr[i])
    maxVal = max(maxVal, dp[i])

print("%.3f" % maxVal)


