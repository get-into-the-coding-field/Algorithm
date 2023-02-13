# 25개 중 7개의 조합들 중에 
# S가 4개 이상인 것들에서
# BFS 실행

from itertools import combinations
from collections import deque

classes = []
lists = [(i, j) for i in range(5) for j in range(5)]
combi = list(combinations(lists, 7))
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
answer = 0

for i in range(5):
    classes.append(list(input().strip()))

def bfs(arr):
    global answer
    visited = [[0] * 5 for _ in range(5)]
    
    q = deque()
    q.append(arr[0])
    visited[arr[0][0]][arr[0][1]] = 1
    sevenPrincess = [0] * 7
    sevenPrincess[0] = 1
    
    while q:
        x, y = q.popleft()
        
        # isFind = False
        
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if (nx, ny) in arr:
                    q.append((nx, ny))
                    sevenPrincess[arr.index((nx, ny))] = 1


        
    if sum(sevenPrincess) == 7:
        # print(f'정답!!!', arr)
        answer += 1
        
for c in combi:
    count = 0
    for i in c:
        if classes[i[0]][i[1]] == 'S':
            count += 1
    
    if count >= 4:
        bfs(c)        
    
print(answer)