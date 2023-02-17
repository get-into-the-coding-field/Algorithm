import heapq as hq
import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    minHeap = [] 
    maxHeap = []
    maps = defaultdict(int)
    
    # heap queue 2개를 사용해서 이중우선순위 큐 구현
    for i in range(n):
        order, num = input().split()
        num = int(num)
        
        if order == 'I':
            hq.heappush(maxHeap, -num)
            hq.heappush(minHeap, num)
            maps[num] += 1
        else:            
            if num == 1:
                while len(maxHeap) > 0:
                    popNum = -hq.heappop(maxHeap)
                    if maps[popNum] > 0:
                        maps[popNum] -= 1
                        break

            
            if num == -1:
                while len(minHeap) > 0:
                    popNum = hq.heappop(minHeap)
                    if maps[popNum] > 0:
                        maps[popNum] -= 1
                        break
    copiedMaps = maps.copy()
    for (key, val) in copiedMaps.items():
        if val == 0:
            maps.pop(key)
        
    if maps:
        print(max(maps), min(maps))
    else:
        print("EMPTY")
        
'''
1
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
'''