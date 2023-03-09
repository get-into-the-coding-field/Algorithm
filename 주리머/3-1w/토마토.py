'''
백준 7569. 토마토
https://www.acmicpc.net/problem/7569

5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1

-1

4 3 2
1 1 0 0
1 1 1 0
1 0 1 1
1 1 1 0
-1 -1 -1 -1
1 1 1 -1

0

'''

from collections import deque
N, M, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]
visit = [[[0] * N for _ in range(M)] for _ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    global days
    dq = deque([])
    
    for i in range(H):
        for j in range(M):
            for k in range(N):
                if tomato[i][j][k] == 1 and visit[i][j][k] == 0:
                    dq.append((i, j, k, 0))
                    visit[i][j][k] = 1
    
    while dq:
        x, y, z, day = dq.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if 0 <= nx < H and 0 <= ny < M and 0 <= nz < N:
                if tomato[nx][ny][nz] == 0 and visit[nx][ny][nz] == 0:
                    # 안익은 토마토를 찾으면 토마토를 익힌다.
                    tomato[nx][ny][nz] = 1
                    visit[nx][ny][nz] = 1
                    days = max(days, day + 1)
                    dq.append((nx, ny, nz, day + 1))
        
days = 0
bfs()

for i in range(H):
    for j in range(M):
        if 0 in tomato[i][j]:
            print(-1)
            exit()

# 토마토가 다 익으면 날짜 출력
print(days)
