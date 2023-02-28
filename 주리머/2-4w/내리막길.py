'''
백준 1520(골드3). 내리막길

4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
'''

import sys
input = sys.stdin.readline
m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    count = 0
    
    for i in range(4):
        dx = direction[i][0] + x
        dy = direction[i][1] + y
        
        if 0 <= dx < m and 0 <= dy < n and maps[x][y] > maps[dx][dy]:
            count += dfs(dx, dy)
    dp[x][y] = count
    return dp[x][y]

print(dfs(0, 0))
'''
3 3
5 4 3
4 3 2
3 2 1
'''
