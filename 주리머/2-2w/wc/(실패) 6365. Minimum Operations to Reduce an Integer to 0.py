from collections import deque

def minOperations(n: int):
    limit = 18 # 100000을 만들 수 있는 최대 횟수
    q = deque()
    q.append((n, 0))
    
    while q:
        cur, count = q.popleft()

        for i in range(limit):
            cal = (2 ** i)
            
            if cal > cur * 2:
                break
            
            subtractor = cur - cal
            
            if subtractor < 0:
                continue
            
            if subtractor == 0:
                return count + 1

            q.append((subtractor, count + 1))
            
            adder = cur + cal
            if adder > 100001:
                continue
            
            if adder == 0:
                return count + 1

            q.append((adder, count + 1))
        
print(minOperations(39)) # 3
print(minOperations(54)) # 3
print(minOperations(74415)) # 3

