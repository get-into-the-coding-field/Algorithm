'''
6 20 3
3 2 45
6 1 66
6 2 31
2 4 94
5 3 46
5 2 79
3 1 64
4 3 74
3 5 59
1 6 93
3 6 45
6 4 40
3 4 67
1 3 61
1 2 42
4 2 50
4 1 55
2 6 93
5 4 95
1 4 54

'''
import heapq as hq
import sys

input = sys.stdin.readline
n, m, x = map(int, input().split())
INF = int(1e9)
roads = [[] * n for _ in range(n)]

answer = 0
x -= 1

for _ in range(m):
    s, e, t = map(int, input().split())
    roads[s-1].append((e-1, t))
    
def dijkstra(start):
    v = [0] * (n)
    d = [INF] * (n)
    d[start] = 0
    
    heap = []
    hq.heappush(heap, (0, start))
    
    while heap:
        dist, current = hq.heappop(heap)
        
        if d[current] < dist:
            continue
        
        # 방문처리
        v[current] = 1
        for next, distance in roads[current]:
            cost = dist + distance
            
            if distance != 0 and v[next] == 0 and cost < d[next]:
                    d[next] = d[current] + distance
                    hq.heappush(heap, (cost, next))
    return d

for town in range(n):
    totalDistance = 0
    
    if town != x:
        d = dijkstra(town)
        totalDistance = d[x]  # 마을에서 X까지 최단 거리
    
        nd = dijkstra(x)   
        totalDistance += nd[town]  # X에서 마을까지 최단 거리
        answer = max(answer, totalDistance)
print(answer)    


    