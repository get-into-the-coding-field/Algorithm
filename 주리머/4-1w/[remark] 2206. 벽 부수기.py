'''
백준 2206. 벽 부수기
https://www.acmicpc.net/problem/2206
'''
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)
maps = [list(map(int, input().strip())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
walls = [(0, 0)]

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            walls.append((i,j))
        
answer = INF

def bfs():
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    
    dq = deque()
    dq.append((0, 0, 0))
    
    while dq:
        x, y, wall = dq.popleft()
        
        if x == n-1 and y == m-1:
            return visited[x][y][wall]
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][wall] == 0:
                if maps[nx][ny] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    dq.append((nx, ny, wall))
                
                if wall == 0 and maps[nx][ny] == 1:
                    visited[nx][ny][1] = visited[x][y][wall] + 1
                    dq.append((nx, ny, 1))
    return -1
    
print(bfs())