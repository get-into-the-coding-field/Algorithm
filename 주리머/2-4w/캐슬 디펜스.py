'''
백준 17135. 캐슬 디펜스
'''

import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N, M, D = map(int, input().split())

matrix = []
answer = 0

for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)
    
dx = [0, -1, 0]
dy = [-1, 0, 1]

def kill(archor):
    tmp_matrix = [matrix[i][:] for i in range(N)]
    killed = [[0] * M for i in range(N)]
    result = 0
    
    for i in range(N-1, -1, -1):
        current_killed = []
        
        for a in archor:
            q = deque([(i, a, 1)])
            
            while q:
                x, y, d = q.popleft()
                if tmp_matrix[x][y] == 1:
                    current_killed.append([x, y])
                    if killed[x][y] == 0:
                        killed.append([x, y])
                        result += 1
                    break
                # 최대 사거리가 아직 남았다면 (활을 더 멀리 쏠 수 있다면)
                if d < D:
                    for i in range(3):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        
                        if 0 <= nx < N and 0 <= ny < M:
                            q.append([nx, ny, d+1])
                            
        for x, y in current_killed:
            tmp_matrix[x][y] = 0
                
    return result
        
    

archor_pos = list(combinations([i for i in range(M)], 3))

for a in archor_pos:
    answer = max(answer, kill(a))

print(answer)



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