'''
백준 13913. 숨바꼭질4
https://www.acmicpc.net/problem/13913
'''

'''
걷는다면 
1초 후에 
X-1
X+1
2*X
'''

from collections import deque

def findPath(x):
    arr = []
    tmp = x
    for _ in range(d[x]+1):
        arr.append(tmp)
        tmp = move[tmp]
    
    return ' '.join(map(str, arr[::-1]))
    
def bfs():
    dq = deque([n])
    while dq:
        x = dq.popleft()
        arr = [x-1,x+1,x*2]
        
        if x == m:
            print(d[x])
            return findPath(x)
        
        for next in arr:
            if 0 <= next <= 100000 and d[next] == 0:
                dq.append(next)
                d[next] = d[x] + 1
                move[next] = x

n, m = map(int, input().split())
d = [0] * 100001
move = [0] * 100001
print(bfs())