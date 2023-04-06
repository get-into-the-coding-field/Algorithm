'''
백준 1753. 최단경로
https://www.acmicpc.net/problem/1753
'''

import sys
import heapq as hq
input = sys.stdin.readline

V, E = map(int, input().split())
peak = int(input())

INF = int(1e9)
graphs = [[] for _ in range(V+1)]
d = [INF] * (V+1)


for _ in range(E):
    s, e, w = map(int, input().split())
    graphs[s].append((w, e))

heap = [[0, peak]]

while heap:
    w, e = hq.heappop(heap)
    
    for nw, ne in graphs[e]:
        tot_weight = w + nw
        if d[ne] > tot_weight:
            d[ne] = tot_weight
            hq.heappush(heap, [tot_weight, ne])

for i in range(1, V+1):
    if i == peak:
        print(0)
    else:
        if d[i] == INF:
            print("INF")
        else:
            print(d[i])
