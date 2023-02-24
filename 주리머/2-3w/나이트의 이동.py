from collections import deque
for _ in range(int(input())):
    l = int(input())
    current = list(map(int, input().split()))
    target = list(map(int, input().split()))
    direction = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    answer = 0
    
    q = deque()
    q.append((current, 0))
    visit = [[False] * l for _ in range(l)]
    
    while q:
        current, count = q.popleft()
        
        if current == target:
            answer = count
            break
        
        cx, cy = current
        for i in range(8):
            dx = cx + direction[i][0]
            dy = cy + direction[i][1]
            
            if 0 <= dx < l and 0 <= dy < l and visit[dx][dy] == 0:
                visit[dx][dy] = 1
                q.append(([dx, dy], count + 1))
    
    print(answer)
    
    
    
    