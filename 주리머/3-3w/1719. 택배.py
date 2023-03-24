'''
백준 1719. 택배
https://www.acmicpc.net/problem/1719
'''
import heapq as hq
import sys
input = sys.stdin.readline

# 최단 경로로 갈 경우 거쳐가야하는 경로
# 최단 경로를 1차적으로 이어져있는 곳으로 찾는다.
n, m = map(int, input().split())
INF = int(1e9)
graph = [[] * (n+1) for _ in range(n+1)]
routes = []

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    graph[e].append((s, t))
    
def dijkstra(start):
    # v = [0] * n
    d = [INF] * (n+1)
    route = ['-'] * (n+1)
    d[start] = 0
    heap = []
    hq.heappush(heap, (0, start, [start]))
    
    while heap:
        dist, current, visit = hq.heappop(heap)
        
        if d[current] < dist:
            continue
        
        # 방문처리
        # v[current] = 1
        
        for next, distance in graph[current]:
            cost = dist + distance
            
            if distance != 0 and cost < d[next]:
                d[next] = d[current] + distance
                
                if len(visit) == 1:
                    route[next] = next
                else:
                    route[next] = visit[1]
                hq.heappush(heap, (cost, next, visit + [next]))
    return route[1:]

# 자기 자신으로 가는 비용은 0
# 최단경로를 찾았을 때 [-1]값을 집어넣는다.
for start in range(1, n+1):
    print(*dijkstra(start))
    

