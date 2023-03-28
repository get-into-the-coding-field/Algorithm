'''
백준 1922. 네트워크
https://www.acmicpc.net/problem/1922

6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8

'''
import sys
import heapq as hq
input = sys.stdin.readline

# 크루스칼 알고리즘
def findParents(parents, x):
    if parents[x] != x:
        parents[x] = findParents(parents, parents[x])
    return parents[x]

def unionParents(parents, a, b):
    a = findParents(parents, a)
    b = findParents(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution():
    N = int(input())
    M = int(input())
    answer = 0
    parents = [i for i in range(N+1)]
    
    edges = []
    
    for i in range(M):
        s, e, d = map(int, input().split())    
        edges.append((d, s, e))
    
    edges.sort()
    
    # 종료 조건: 모든 노드가 연결되었을 때
    for distance, start, end in edges:
        if findParents(parents, start) == findParents(parents, end):
            continue
        else:
            unionParents(parents, start, end)
            answer += distance
    return answer

print(solution())


# 프림 알고리즘
def solution():
    N = int(input())
    M = int(input())
    vertex = []
    edges = [[] for _ in range(N+1)]
    answer = 0
    mst = []
    
    
    for _ in range(M):
        s, e, d = map(int, input().split())
        edges[s].append((d, e))
        edges[e].append((d, s))


    # 정점 1 방문처리
    for d, e in edges[1]:
        hq.heappush(vertex, (d, e))
    mst.append(1)
    
    
    while vertex:
        distance, end = hq.heappop(vertex)

        if end not in mst:    
            mst.append(end)
            answer += distance
            
            for d, e in edges[end]:
                hq.heappush(vertex, (d, e))

    return answer

print(solution())