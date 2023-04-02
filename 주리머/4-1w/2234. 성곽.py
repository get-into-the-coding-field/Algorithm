'''
백준 2234. 성곽
https://www.acmicpc.net/problem/2234

7 4
11 6 11 6 3 10 6
7 9 6 13 5 15 5
1 10 12 7 13 7 5
13 11 10 8 10 12 13

'''

'''
dfs 이용

서쪽에 벽이 있을 때는 1을, 북쪽에 벽이 있을 때는 2를, 동쪽에 벽이 있을 때는 4를, 남쪽에 벽이 있을 때는 8을 더한 값이 주어진다. 
이진수

[SENW]
1111
'''
from collections import defaultdict
from collections import deque

adjacent_dict = defaultdict(set)
size_dict = defaultdict(int)
room_route_dict = defaultdict(set)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir = ["S", "E", "N", "W"]
m, n = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]
castle_size = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

room_cnt = 0
largest_room_size = 0
final_largest_room_size = 0

def bfs():
    global room_cnt
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                room_cnt += 1
                room_route_dict[(i,j)].add((i,j))
                
                q = deque()
                q.append((i, j))
                
                while q:
                    x, y = q.popleft()
                    binary = bin(castle[x][y])[2:].zfill(4)
                    
                    for b in range(4):
                        # 벽이 뚫려 있으면
                        if binary[b] == "0":
                            nx = x + dx[b]
                            ny = y + dy[b]
                            
                            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                room_route_dict[(i,j)].add((nx, ny))
                                    
                                q.append((nx, ny))
                    
bfs()

# 인접한 값 넣기

for k, v in room_route_dict.items():
    
    for x, y in v:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in room_route_dict[(k[0], k[1])]:
                adjacent_dict[(x, y)].add((nx, ny))

# 방마다 size 넣기
for k, v in room_route_dict.items():
    size = len(room_route_dict[k])
    
    for x, y in v:
        castle_size[x][y] = size

# 인접한 방의 크기 합의 최댓값
for k, v in adjacent_dict.items():
    for x, y in v:
        if (x, y) not in room_route_dict[(k[0], k[1])] and final_largest_room_size < castle_size[k[0]][k[1]] + castle_size[x][y]:
            final_largest_room_size = castle_size[k[0]][k[1]] + castle_size[x][y]


print(room_cnt)
print(max(sum(castle_size, [])))
print(final_largest_room_size)



# 9 9 3 3 8 8 8
# 9 9 9 3 8 0 8
# 9 9 9 7 8 7 8
# 9 7 7 7 7 7 8
