import sys
from collections import deque
input = sys.stdin.readline
n = int(input()) # 간선의 개수
tree = [[] for _ in range(n + 1)]
diameter = 0

for i in range(n-1):
    a, b, weight = map(int, input().split()) 
    tree[a].append((b, weight))
    tree[b].append((a, weight))


def bfs(arr):
    i, total = arr
    q = deque()
    q.append((i, 0, [i]))
    farthest = [i, total] # 가장 먼 노드값, 가중치
    
    while q:
        node, total, visit = q.popleft()
        if total > farthest[1]:
            farthest[0] = node
            farthest[1] = total

        for (j, weight) in tree[node]:
            if j not in visit:
                visit.append(j)
                q.append((j, total + weight, visit))
    return farthest

print(bfs(bfs([1, 0]))[1])