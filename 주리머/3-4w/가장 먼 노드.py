'''
프로그래머스 lv3. 가장 먼 노드
https://school.programmers.co.kr/learn/courses/30/lessons/49189
'''

'''
1번 노드부터 최단거리로 이동할 수 있는 노드를 찾는다.
최단거리를 저장하는 배열과 이동 거리를 저장하는 노드를 찾는다.

다익스트라 알고리즘 + 배열 사용
'''
import heapq as hq

def solution(n, vertexs):    

    
    def dijktra(start):
        d = [INF] * (n+1)
        d[start] = 0    
        heap = []
        
        hq.heappush(heap, (0, start))
        
        while heap:
            dist, cur_node = hq.heappop(heap)
            
            
            for next_node in edges[cur_node]:
                if d[next_node] > dist + 1:
                    d[next_node] = dist + 1
                    hq.heappush(heap, (d[next_node], next_node))
            
        
        max_cnt = max([i for i in d if i != INF])
        return d.count(max_cnt)

    INF = int(1e9)
    edges = [[] for _ in range(n+1)]
    
    for start, end in vertexs:
        edges[start].append(end)
        edges[end].append(start)
        
    return dijktra(1)

'''
bfs 풀이
'''
from collections import deque
from collections import defaultdict
def solution2(n, vertexs):
    
    def bfs():
        dq = deque()
        dq.append((0, 1))
        visit[1] = True
        while dq:
            cnt, cur_node = dq.popleft()
            dict[cnt] += 1
            
            for next_node in edges[cur_node]:
                if not visit[next_node]:
                    visit[next_node] = True
                    dq.append((cnt+1, next_node))
                    
            
    INF = int(1e9)
    edges = [[] for _ in range(n+1)]
    visit = [False] * (n+1)
    dict = defaultdict(int)
    for start, end in vertexs:
        edges[start].append(end)
        edges[end].append(start)
    
    bfs()
    return dict[max(dict.keys())]
    
print(solution2(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))