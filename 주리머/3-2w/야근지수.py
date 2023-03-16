import heapq as hq

def solution(n, works):
    arr = []
    
    if sum(works) < n:
        return 0
    
    for w in works:
        hq.heappush(arr, -w)
        
    while n:
        num = hq.heappop(arr)
        num += 1
        
        hq.heappush(arr, num)
        n -= 1
    
    return sum([i ** 2 for i in arr])

# 큰 수를 무조건 줄이는 게 도움이 된다.
# print(solution(4, [4, 3, 3]))
# print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
# print(solution(5, [1, 100, 2]))
# print(solution(7, [3, 10, 9]))
# print(solution(999, [800, 100, 55, 45]))