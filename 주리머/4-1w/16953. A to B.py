'''
백준 16953. A to B
https://www.acmicpc.net/problem/16953
'''
from collections import deque


def plus_one(a):
    return a * 10 + 1

def solution():
    A, B = map(int, input().split())
    # 이분 검색이 가능하므로 visited 생략
    # visited = [False] * (limit+1)
    
    dq = deque()
    dq.append((A, 0))
    
    while dq:
        a, cnt = dq.popleft()
        
        # print(f'a: {a}, cnt: {cnt}')
        if a == B:
            return cnt + 1
        
        for na in (a*2, plus_one(a)):
            if 1 <= na <= limit:
                dq.append((na, cnt+1))
    
    return -1

limit = int(1e9)
print(solution())