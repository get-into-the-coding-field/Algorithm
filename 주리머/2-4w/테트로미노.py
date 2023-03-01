'''
백준 14500. 테크로미노
https://www.acmicpc.net/problem/14500
'''
def solution():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # ㅗ(h) 모양
    figureH = [
            [(0, 0), (1, 0), (1, -1), (1, 1)],
            [(0, 0), (0, 1), (0, 2), (1, 1)],
            [(0, 0), (1, 0), (1, -1), (2, 0)],
            [(0, 0), (1, 0), (1, 1), (2, 0)],
    ]
    global answer
    answer = 0
    
    def dfs(x, y, count, total):
        
        if count == 4:
            global answer
            answer = max(answer, total)
            return
        
        for i in range(4):
            
            mx = dx[i] + x
            my = dy[i] + y
                
            if 0 <= mx < n and 0 <= my < m and visit[mx][my] == 0:
                visit[mx][my] = 1
                dfs(mx, my, count+1, total+arr[mx][my])
                visit[mx][my] = 0
        return 
        
    for i in range(n):
        for j in range(m):
            visit[i][j] = 1
            dfs(i, j, 1, arr[i][j])
            visit[i][j] = 0
    
    "ㅗ 모양 만들기"
    def makeTetromino(x, y):
        global answer
        for figure in figureH:
            total = 0
            for i in figure:
                
                dx, dy = i
                if 0 <= x + dx < n and 0 <= y + dy < m:
                    total += arr[x + dx][y + dy]
                    continue
                else:
                    break
            answer = max(answer, total)
                    
    
    for i in range(n):
        for j in range(m):
            makeTetromino(i, j)
    
    return answer

print(solution())
