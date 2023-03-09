# 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.

'''
백준 16236. 아기상어
https://www.acmicpc.net/problem/16236

4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4

14
'''

from collections import deque
import heapq as hq
import sys 
input = sys.stdin.readline

n = int(input())
seas = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
days = 0

def bfs():
    global days
    dq = deque([])
    breakpoint = False
    
    for i in range(n):
        for j in range(n):    
            if seas[i][j] == 9:
                dq.append((i, j, 2, 1, 0, 0, [(i, j)], []))
                seas[i][j] = 0
                breakpoint = True
                break
        
        if breakpoint:
            break
                
    while dq:
        x, y, level, distance, feed, time, visit, will_feed = dq.popleft()
        
        # 현재 거리 이전에 짧은 거리에 먹을 물고기가 존재한다면
        if will_feed and distance > will_feed[0][0]:
                    # 먹이를 먹으면 dq를 초기화하고 다시 q에 넣는다.
                    # 아기 상어 크기 이하라면 먹고 해당 위치로 이동
                    # 먹은 위치 빈 값 처리
                    # print(f'현재까지 먹을 수 있는 물고기들: {will_feed}')
                    dist, wx, wy = hq.heappop(will_feed) 
                    seas[wx][wy] = 0
                    feed += 1
                    # print(f'먹은 위치 {wx, wy}, 먹는 물고기 level: {seas[wx][wy]} exp: {feed} 이동 거리: {dist}, 현재 초: {time + dist}')
                    
                    if feed == level:
                        # print(f'level up {level} -> {level + 1}')
                        level += 1
                        feed = 0
                    
                    # 지나간 기록 초기화
                    visit = [(wx, wy)]
                    dq = deque([])
                    dq.append((wx, wy, level, 1, feed, time + dist, visit, []))
                    continue
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visit:
                # 아기상어보다 레벨이 작은 경우
                if 0 < seas[nx][ny] < level:
                    hq.heappush(will_feed, [distance, nx, ny])
                    dq.append((nx, ny, level, distance + 1, feed, time, visit, will_feed))
                
                elif seas[nx][ny] <= level and (nx, ny) not in visit:
                    visit.append((nx, ny))
                    dq.append((nx, ny, level, distance + 1, feed, time, visit, will_feed))
        else:
            # print(f'바다 ======')
            # for i in seas:
            #     print(i)
            days = max(days, time)


bfs()
print(days)
