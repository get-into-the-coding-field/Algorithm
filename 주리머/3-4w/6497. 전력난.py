'''
백준 6497. 전력난
https://www.acmicpc.net/problem/6497
'''
import sys
import heapq as hq
input = sys.stdin.readline

# 최대값을 구하고 
# MST 구해서 빼기
while True:
    n, m  = map(int, input().split())
    
    if m == 0 and n == 0:
        break
    
    edges = [[] for _ in range(n+1)]
    visit = [False] * (n+1)
    mst = []
    max_cost = 0
    mst_cost = 0
    cnt = 0
    
    for _ in range(m):
        s, e, d = map(int, input().split())
        edges[s].append((d, e))
        edges[e].append((d, s))
        max_cost += d
    
    for dist, dest in edges[1]:
        hq.heappush(mst, (dist, dest))
    visit[1] = True
    
    while mst:
        cur_cost, cur_node = hq.heappop(mst) 
        
        
        if not visit[cur_node]:
            mst_cost += cur_cost
            visit[cur_node] = True
            cnt += 1
            
            if cnt == n:
                break
                    
            for next_cost, next_node in edges[cur_node]:
                hq.heappush(mst, (next_cost, next_node))
    print(max_cost - mst_cost)
