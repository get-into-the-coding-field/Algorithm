'''
백준 2665. 미로만들기
https://www.acmicpc.net/problem/2665

8
11100110
11010010
10011010
11101100
01000111
00110001
11011000
11000111

'''

from collections import deque
import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    maze = []
    
    for _ in range(n):
        maze.append(list(input().strip()))
    
    def bfs():
        dq = deque([(0, 0)])
        visit = [[-1] * n for _ in range(n)]
        visit[0][0] = 0

        while dq:
            x, y = dq.popleft()
            
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                
                if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == -1:
                    # maze가 흰방이면 큐 맨 처음에 넣는다.
                    if maze[nx][ny] == "1":
                        visit[nx][ny] = visit[x][y]
                        dq.appendleft((nx, ny)) 
                    # maze가 검은방이면 큐 마지막에 넣는다.
                    else:
                        visit[nx][ny] = visit[x][y] + 1
                        dq.append((nx, ny))
    
                    if nx == n-1 and ny == n-1:
                        return visit[n-1][n-1]
    return bfs()    

print(solution())