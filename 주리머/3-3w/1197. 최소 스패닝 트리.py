'''
백준 1197. 최소 스패닝 트리
https://www.acmicpc.net/problem/1197

3 3
1 2 1
2 3 2
1 3 3

'''

def findParents(parents, x):
    if parents[x] == x:
        return x
    return findParents(parents, parents[x])

def unionParents(parents, x, y):
    a = findParents(parents, x)
    b = findParents(parents, y)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution():
    N, M = map(int, input().split())
    edges = []
    parents = [i for i in range(N+1)]
    answer = 0
    
    for _ in range(M):
        s, e, d = map(int, input().split())
        edges.append((d, s, e))    
    edges.sort()
    
    for distance, start, end in edges:
        if findParents(parents, start) == findParents(parents, end):
            continue
        else:
            unionParents(parents, start, end)
            answer += distance
    return answer

print(solution())