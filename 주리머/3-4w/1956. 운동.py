
'''
백준 1956. 운동
https://www.acmicpc.net/problem/1956

3 4
1 2 1
3 2 1
1 3 5
2 3 2


'''

'''
다익스트라
'''

# import heapq as hq
                
# def solution():
    
#     def dijkstra():

#         while heap:
#             d, s, nd = hq.heappop(heap)

#             if s == nd:
#                 return d
            
#             if dArr[s][nd] < d:
#                 continue            

#             for distance, next_node in edges[nd]:
#                 cost = d + distance
                
#                 if distance != 0 and cost < dArr[s][next_node]:
#                         dArr[s][next_node] = cost
#                         hq.heappush(heap, (cost, s, next_node))
#         # 사이클을 못 찾은 경우
#         return -1

#     n, m = map(int, input().split())
    
#     if m <= 1:
#         return -1
    
#     INF = int(1e9)
#     edges = [[] for _ in range(n+1)]
#     heap = []
#     dArr = [[INF] * (n+1) for _ in range(n+1)]

#     for _ in range(m):
#         s, e, d = map(int, input().split())
#         edges[s].append((d, e))
#         dArr[s][e] = min(dArr[s][e], d)
#         hq.heappush(heap, (d, s, e))
    
#     return dijkstra()

# print(solution())


'''
플로이드 와샬
'''



def solution():
    
    def floyd():
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):                
                    if edges[i][j] > edges[i][k] + edges[k][j]:
                        edges[i][j] = edges[i][k] + edges[k][j]
                    
    n, m = map(int, input().split())
    INF = int(1e9)
    edges = [[INF] * (n+1) for _ in range(m+1)]
    
    for _ in range(m):
        s, e, d = map(int, input().split())
        edges[s][e] = d
    
    floyd()
    
    answer = INF
    for i in range(1, n+1):
        answer = min(answer, edges[i][i]) 
    
    return -1 if answer == INF else answer
    
    
print(solution())