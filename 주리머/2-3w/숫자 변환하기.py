from collections import deque
def solution(x, y, n):
    visit = [0] * 1000001
    q = deque()
    q.append((x, 0))
    
    if not(y % 2 == 0 or y % 3 == 0 or y % n == x):
        return -1
    
    while q:
        a, count = q.popleft()
        
        if a == y:
            return count
        
        if a + n <= 1000000 and visit[a + n] == 0:
            visit[a + n] = 1
            q.append((a + n, count + 1))
        
        if a * 2 <= 1000000 and visit[a * 2] == 0:
            visit[a * 2] = 1
            q.append((a * 2, count + 1))
            
        if a * 3 <= 1000000 and visit[a * 3] == 0:
            visit[a * 3] = 1
            q.append((a * 3, count + 1))
    return -1
    
print(solution(10, 40, 5)) # 2
print(solution(10, 40, 30)) # 1
print(solution(2, 5, 4)) # -1

