'''
백준 13549. 숨바꼭질3
https://www.acmicpc.net/problem/13549
'''

from collections import deque
from collections import defaultdict
n, m = map(int, input().split())
case_number = 100001
visit = [False] * 100001

def bfs():
    
    dq = deque()
    dq.append((n, 0))
    
    while dq:
        x, count = dq.popleft()
        visit[x] = True
        
        if x == m:
            return count
        
        if 0 <= x*2 <= 100000 and not visit[x*2]:
            dq.append((x*2, count))
            
        if 0 <= x-1 <= 100000 and not visit[x-1]:
            dq.append((x-1, count+1))
        
        if 0 <= x+1 <= 100000 and not visit[x+1]:
            dq.append((x+1, count+1))
            
            
print(bfs())






