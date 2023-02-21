n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], (arr[j] + dp[i-j]))
        

print(dp[n])
'''
4
1 5 6 7

5
10 9 8 7 6

4
5 2 8 10
'''


# 1번으로 살 수 있는 최대 값
# 2번으로 살 수 있는 최대 값