'''
백준 11657. 타임머신
https://www.acmicpc.net/problem/11657

3 4
1 2 4
1 3 3
2 3 -1
3 1 -2

'''

n, m = map(int, input().split())
INF = int(1e9)
edges = []
dist = [INF] * (n+1)
def bellmanFord(start):

    # 초기화
    dist[start] = 0
    
    for i in range(n):
        for j in range(m):
            cur, next, cost = edges[j][0], edges[j][1], edges[j][2]
            
            if dist[cur] != INF and dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                
                # 마지막에 갱신이 되었다면 음수 사이클이 존재
                if i == n-1:
                    return True
    return False

for _ in range(m):
    s, e, t = map(int, input().split())
    edges.append((s, e, t))

# 벨만포드 알고리즘
isNegativeCycle = bellmanFord(1) # 1번 노드에서 시작

if isNegativeCycle:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
            