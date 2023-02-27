'''
이동하기
https://www.acmicpc.net/problem/11048

3 4
1 2 3 4
0 0 0 5
9 8 7 6
'''

n, m = map(int, input().split())


maze = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (m) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0:
            if j == 0:
                dp[i][j] = maze[i][j]
                continue
            dp[i][j] = dp[i][j-1] + maze[i][j]
            continue
        if j == 0:
            dp[i][j] = dp[i-1][j] + maze[i][j]
            continue
        
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + maze[i][j]
    
print(dp[n-1][m-1])
