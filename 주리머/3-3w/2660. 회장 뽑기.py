'''
백준 2660. 회장 뽑기
https://www.acmicpc.net/problem/2660

5
1 2
2 3
3 4
4 5
2 4
5 3
-1 -1

'''

n = int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

while True:
    s, e = map(int, input().split())
    if s == -1 and e == -1:
        break
    
    graph[s][e] = 1
    graph[e][s] = 1

distance = [INF] * (n+1)

for k in range(1, n+1):
    for i in range(1, n+1):
        if i == k:
            continue
        for j in range(1, n+1):
            if i == j:
                continue
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

score = INF
candidate = []

for i in range(1, n+1):
    maxScore = max([g for g in graph[i] if g != INF])
    
    if score > maxScore:
        score = maxScore
        candidate = [i]
    elif score == maxScore:
        candidate.append(i)

print(score, len(candidate))
print(*candidate)
    
    
