import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
maps = []
result = [[0] * m for _ in range(n)]

for i in range(n):
    maps.append(list(map(int, input().split())))

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visit = [[0] * m for _ in range(n)]

for i in range(n):
    isFind = False
    for j in range(m):
        if maps[i][j] == 2:
            q = deque()
            q.append((i, j, 0))
            visit[i][j] = 1
            
            while q:
                x, y, count = q.popleft()
                
                result[x][y] = count
                
                for c in range(4):
                    nx = x + direction[c][0]
                    ny = y + direction[c][1]
                    
                    if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        # 막혀있는 곳
                        if maps[nx][ny] == 0:
                            result[nx][ny] = 0
                            continue
                        
                        q.append((nx, ny, count + 1))
            isFind = True
            break      
    if isFind:
        break

for i in range(n):
    for j in range(m):
        if maps[i][j] != 0 and visit[i][j] == 0:
            result[i][j] = -1
            
for i in result:
    print(*i)
            
            
            
            
'''
15 15
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
'''