'''
백준 1647. 도시 분할 계획
https://www.acmicpc.net/problem/1647
'''

import heapq as hq
import sys
input = sys.stdin.readline

'''
크루스칼 알고리즘
'''

# 부모값 찾기
def getParent(parents, x):
    if parents[x] == x:
        return x
    return getParent(parents, parents[x])

# 같은 부모값인지 확인
def findParents(parents, x, y):
    a = getParent(parents, x)
    b = getParent(parents, y)
    
    if a == b:
        return 1
    return 0

# 부모값 합치기
def unionParents(parents, x, y):
    a = getParent(parents, x)
    b = getParent(parents, y)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
    
def solution():
    N, M = map(int, input().split())
    edges = []
    cities = [i for i in range(N+1)]
    answer = 0
    count = 0
    
    for _ in range(M):
        s, e, d = map(int, input().split())
        edges.append((d, s, e))
    
    edges.sort()
    
    # print(f'edges: {edges}')
    for distance, start, end in edges:
        # 이미 연결되어있다면 pass
        if findParents(cities, start, end):
            continue
        
        # 연결이 아직 안되어있다면 연결하기
        # print(f'unionParents 동작: {start}, {end}, cities : {cities}, dist:{distance}')
        unionParents(cities, start, end)
        # print(f'unionParents 동작 완료: cities : {cities}')
        answer += distance
        count += 1
        
        # 간선 정보가 꽉 찼기 때문
        if count == N-2:
            break
        
    # print(f'cities : {cities}')
    return answer

print(solution())

'''
프림 알고리즘
'''

def solution():
    N, M = map(int, input().split())
    vertex = []
    edges = [[] for _ in range(N+1)]
    visit = [False] * (N+1)
    answer = []
    mst = []
    
    
    for _ in range(M):
        s, e, d = map(int, input().split())
        edges[s].append((d, e))
        edges[e].append((d, s))


    # 정점 1 방문처리
    for d, e in edges[1]:
        hq.heappush(vertex, (d, e))
    visit[1] = True
    
    while vertex:
        cost, node = hq.heappop(vertex)

        if not visit[node]:    
            answer.append(cost)
            visit[node] = True
            
            if len(answer) == N:
                break
            
            for d, e in edges[node]:
                # 방문하지 않은 노드만 추가
                if not visit[e]:
                    hq.heappush(vertex, (d, e))
    return sum(answer) - max(answer)

print(solution())