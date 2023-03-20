'''

'''

from collections import deque

def solution(n, m, picture):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    tot = 0
    maxTot = 0
    
    def bfs(x, y):
        
        dq = deque([(x, y)])    
        cnt = 1
        
        while dq:
            x, y = dq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if picture[nx][ny] == picture[x][y] and visit[nx][ny] == 0:
                        cnt += 1
                        visit[nx][ny] = 1
                        dq.append((nx, ny))
        return cnt
    visit = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if picture[i][j] != 0 and visit[i][j] == 0:
                visit[i][j] = 1
                tot += 1
                maxTot = max(maxTot, bfs(i, j))
    
    return [tot, maxTot]
print(solution(6,4,[[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]))