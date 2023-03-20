'''
1051. 숫자 정사각형
https://www.acmicpc.net/problem/1051

3 5
42101
22100
22101
'''

# 꼭짓점 사각형 = 우, 밑, 대각선

from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dx = [1, 0, 1]
dy = [0, 1, 1]
answer = 1


for i in range(n):
    for j in range(m):
        dq = deque([(arr[i][j], i, j, 1)])
        
        while dq:
            num, x, y, cnt = dq.popleft()
            
            isQuad = True
            round = 0
            for k in range(3):
                nx = dx[k] * cnt + x
                ny = dy[k] * cnt + y
                
                
                if 0 <= nx < n and 0 <= ny < m:
                    round += 1
                    
                    if num != arr[nx][ny]:
                        isQuad = False
                else:
                    break
            else:
                dq.append((num, x, y, cnt+1))
                if isQuad:
                    answer = max(answer, (cnt+1) ** 2)  
print(answer)
                
            