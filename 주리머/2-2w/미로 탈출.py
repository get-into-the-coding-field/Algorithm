from collections import deque
def solution(maps):
    maps = [list(i) for i in maps]
    n = len(maps)
    m = len(maps[0])
    start = ()
    lever = ()
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    isFind = [0, 0]
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                start = (i, j)
                isFind[0] = 1
            if maps[i][j] == "L":
                lever = (i, j)
                isFind[1] = 1

            if sum(isFind) == 2:
                break
    
    def bfs(x, y, count, isOpen):
        q = deque()
        q.append((x, y, count, isOpen))
        visit = [[0] * m for _ in range(n)]
        visit[x][y] = 1
        
        while q:
            x, y, count, isOpen = q.popleft()

            for i in range(4):
                dx = x + direction[i][0]
                dy = y + direction[i][1]
                
                if 0 <= dx < n and 0 <= dy < m and maps[dx][dy] != "X" and visit[dx][dy] == 0:
                    if maps[dx][dy] == "L":
                        return count + 1
                    
                    if maps[dx][dy] == "E" and isOpen == 1:
                        return count + 1
                    
                    visit[dx][dy] = 1
                    q.append((dx, dy, count + 1, isOpen))
        return - 1
    countUntilLever = bfs(start[0], start[1], 0, 0)
    
    if countUntilLever > 0:
        result = bfs(lever[0], lever[1], countUntilLever, 1)
        
        return result
    return -1

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])) # 16
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])) # -1