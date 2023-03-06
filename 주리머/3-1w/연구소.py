'''
백준 14502. 연구소
https://www.acmicpc.net/problem/14502

7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''

from itertools import combinations
from collections import deque
import copy

def spread_virus(additory_walls):
    virtual_maps = copy.deepcopy(maps)
    
    # 가상의 벽 생성
    for ad in additory_walls:
        virtual_maps[ad[0]][ad[1]] = 1
    
    # 바이러스 퍼뜨리기
    for virus in viruses:
        q = deque()    
        q.append((virus[0], virus[1]))
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and virtual_maps[nx][ny] == 0:
                    if virtual_maps[nx][ny] == 0:
                        virtual_maps[nx][ny] = 2
                        q.append([nx, ny])
    # 남은 영역 계산
    cnt = 0
    
    for i in range(n):
        cnt += virtual_maps[i].count(0)
    
    return cnt
                        

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
empty = []
viruses = []

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            empty.append([i, j])
        
        if maps[i][j] == 2:
            viruses.append([i, j])

combi = list(combinations(empty, 3))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]                
answer = 0
    
for c in combi:
    answer = max(answer, spread_virus(c))

print(answer)