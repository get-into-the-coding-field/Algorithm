'''
백준 1167. 트리의 지름
https://www.acmicpc.net/problem/1167
'''
import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
vertex = [[] for _ in range(n+1)]

for _ in range(n):
    arr = list(map(int, input().split()))[:-1]
    peak =  arr[0]
    
    for i in range(3, len(arr) + 1, 2):
        o_peak, dis = arr[i-2:i]
        vertex[peak].append((o_peak, dis))
        
    

def bfs(start):
    visit = [-1] * (n+1)
    dq = deque()
    dq.append((start))
    max_node = [0, 0]
    visit[start] = 0
    
    while dq:
        current = dq.popleft()
        for next, dis in vertex[current]:
            if visit[next] == -1:
                visit[next] = visit[current] + dis    
                
                if visit[next] > max_node[1]:
                    max_node = [next, visit[next]]
                dq.append((next))
                
    return max_node
    
node, dis = bfs(1)
node, dis = bfs(node)

print(dis)
    
        
    
    