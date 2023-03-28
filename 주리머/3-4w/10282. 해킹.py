'''
백준 10282. 해킹
https://www.acmicpc.net/problem/10282
'''

'''
다익스트라
'''
import sys
import heapq as hq
input = sys.stdin.readline
INF = int(1e9)

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    
    computers = [[] for _ in range(n+1)]
    
    for _ in range(d):
        b, a, t = map(int, input().split())
        computers[a].append((t, b))
    
    infection = [INF] * (n+1)
    infection[c] = 0
    heap = []
    hq.heappush(heap, (0, c))

    while heap:
        cur_time, cur_computer = hq.heappop(heap)
        
        if infection[cur_computer] < cur_time:
            continue
        
        for next_time, next_computer in computers[cur_computer]:
            tot_time = cur_time + next_time
            if tot_time < infection[next_computer]:
                    
                infection[next_computer] = tot_time
                hq.heappush(heap, (tot_time, next_computer))    
    
    final_time = -1
    cnt = 0
    
    for i in range(1, n+1):
        if infection[i] != INF:
            cnt += 1
            final_time = max(final_time, infection[i])

    print(cnt, final_time)
