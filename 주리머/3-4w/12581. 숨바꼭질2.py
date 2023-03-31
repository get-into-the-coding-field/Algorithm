'''
백준 12851. 숨바꼭질2
https://www.acmicpc.net/problem/12851
'''
from collections import deque
from collections import defaultdict
n, m = map(int, input().split())
case_number = 100001
visit = [False] * 100001
countDict = defaultdict(int)

def bfs():
    
    dq = deque()
    dq.append((n, 0))
    
    while dq:
        x, count = dq.popleft()
        visit[x] = True
        
        if x == m:
            countDict[count] += 1
        
        for y in (x-1, x+1, x*2):
            if 0 <= y <= 100000 and not visit[y]:
                dq.append((y, count+1))

bfs()

for key in countDict.keys():
    if key == min(countDict.keys()):
        print(key)
        print(countDict[key])




