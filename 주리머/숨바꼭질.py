from collections import deque

n, m = map(int, input().split())
visit = [0] * 100002
q = deque()

if n == m:
    print(0)
else:
    q.append((n, 0))

    while q:
        a, count = q.popleft()
        
        if a + 1 <= 100000 and visit[a + 1] == 0:
            if a + 1 == m:
                print(count + 1)
                break
            q.append((a + 1, count + 1))
            visit[a + 1] = 1
        
        if a - 1 >= 0 and visit[a - 1] == 0:
            if a - 1 == m:
                print(count + 1)
                break
            q.append((a - 1, count + 1))
            visit[a - 1] = 1
        
        if a * 2 <= 100000 and visit[a * 2] == 0:
            if a * 2 == m:
                print(count + 1)
                break
            q.append((a * 2, count + 1))
            visit[a * 2] = 1

    '''
    10000 10000 -> 1

    '''