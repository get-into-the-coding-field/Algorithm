
import heapq as hq
# 다익스트라 풀이
def solution(N, road, K):
    delivery = [500001] * (N + 1)
    delivery[1] = 0
    time = [[] for _ in range(N+1)]
    
    def dijkstra(delivery, time):
        heap = []
        hq.heappush(heap, [0, 1]) # 거리, 노드
        
        while heap:
            cost, node = hq.heappop(heap)
            
            for c, n in time[node]:
                if cost + c <= delivery[n]:
                    delivery[n] = cost + c
                    hq.heappush(heap, [cost + c, n])
                    
    for r in road:
        time[r[0]].append([r[2], r[1]])
        time[r[1]].append([r[2], r[0]])

    dijkstra(delivery, time)
    return len([i for i in delivery if i <= K])


print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))