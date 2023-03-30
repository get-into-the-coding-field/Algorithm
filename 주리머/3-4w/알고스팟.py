'''
백준 1261. 알고스팟
https://www.acmicpc.net/problem/1261
'''

from collections import deque

n, m = map(int, input().split())
blocks = []

if n == 1 and m == 1:
    print(0)
    exit()
    
for _ in range(m):
    blocks.append(list(input().strip()))

visit = [[-1] * (n) for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    dq = deque([(0, 0)])
    
    while dq:
        x, y = dq.popleft()
        visit[0][0] = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == -1:
                
                # 막혀있는 벽일 경우 부수고 이동 (+1)
                if blocks[nx][ny] == '1':
                    visit[nx][ny] = visit[x][y] + 1
                    dq.append((nx, ny))
                # 뚫려있을 경우 안 부수고 (이전 값과 동일) 이동
                else:
                    visit[nx][ny] = visit[x][y]
                    dq.appendleft((nx, ny))
                    
                # 마지막 점에 도달하면 이전 visit값을 반환한다        
                if nx == m-1 and ny == n-1:
                    return visit[x][y]
print(bfs())
