from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, dist = map(int, input().split())
    arr[a].append((b, dist))
    arr[b].append((a, dist))

for _ in range(m):
    a, b = map(int, input().split())
    visit = [0] * (n + 1)
    q = deque()
    q.append((a, 0))
    visit[a] = 1
    
    while q:
        node, dist = q.popleft()
        
        
        for (i, weight) in arr[node]:
            if visit[i] == 0:
                if i == b:
                    print(dist + weight)
                    break
                
                visit[i] = 1
                q.append((i, dist + weight))
    