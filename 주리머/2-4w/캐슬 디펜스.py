'''
백준 17135. 캐슬 디펜스
https://www.acmicpc.net/problem/17135
'''



# 궁수 3명 자리 배치
# 성에 가깝게 배치,, 가장 가까운 좀비와의 사거리가 닿는 곳 이내에
'''
5 5 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
'''

from itertools import combinations
from collections import deque
import copy

n, m, D = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
answer = 0
direction = [(0, -1), (-1, 0), (0, 1)]

    
    
def shoot_arrow(archers):
    tmp_maps = [maps[i][:] for i in range(n)]
    killed = [[0] * m for _ in range(n)]
    count = 0
    
    for i in range(n-1, -1, -1):
        this_turn = []
        
        for a in archers:
            q = deque([])
            q.append((i, a, 1))
            
            while q:
                x, y, d = q.popleft()
                
                if tmp_maps[x][y] == 1:
                    this_turn.append((x, y))

                    if killed[x][y] == 0:
                        killed[x][y] = 1
                        count += 1
                    break
                
                if d < D:
                    for j in range(3):
                        nx = x + direction[j][0]
                        ny = y + direction[j][1]
                        
                        if 0 <= nx < n and 0 <= ny < m:    
                            q.append((nx, ny, d+1))
        for x, y in this_turn:
            tmp_maps[x][y] = 0
    return count
                
archer_combi = list(combinations([i for i in range(m)], 3))
for combi in archer_combi:
    answer = max(answer, shoot_arrow(combi))
    
print(answer)

