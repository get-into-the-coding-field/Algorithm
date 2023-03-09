'''
백준 15686. 치킨 배달
https://www.acmicpc.net/problem/15686

5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

5
'''
from collections import deque
from itertools import combinations


def getDistance(sx, sy, ex, ey):
    return abs(sx - ex) + abs(sy - ey)

def deliver_chicken(arr):
    left_chicken = [ch for ch in chicken_houses if ch not in arr]
    count = 0
    
    for h in houses:
        q = deque()
        q.append((h[0], h[1], h[0], h[1]))
        min_count = 1e9
        
        for lc in left_chicken:
            min_count = min(min_count, getDistance(h[0], h[1], lc[0], lc[1]))
        
        count += min_count
    return count
            
n, m = map(int, input().split())
chicken_houses = []
houses = []
maps = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            chicken_houses.append([i, j])
        if maps[i][j] == 1:
            houses.append([i, j])

chicken_length = len(chicken_houses)
houses_length = len(houses)
combi = list(combinations(chicken_houses, chicken_length - m))
answer = 1e9
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for c in combi:
    answer = min(answer, deliver_chicken(c))

print(answer)    
