'''
백준 16928. 뱀과 사다리 게임
https://www.acmicpc.net/problem/16928


3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17

'''

from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

# 사다리와 뱀의 위치를 저장할 딕셔너리

ladder = {}
snake = {}

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y

visit = [0] * 101
dq = deque([(1, 0, [])])

while dq:
    cur, count, route = dq.popleft()
    
    for i in range(1, 7):
        # print(f'현재 위치는 {cur}이며, 주사위는 {i}입니다.')
        nCur = cur + i
        
        if nCur == 100:
            print(count + 1)
            # print(route)
            exit()
        
        if nCur > 100:
            break
        
        if nCur in ladder:
            nCur = ladder[nCur]
        
        if nCur in snake:
            nCur = snake[nCur]

        if visit[nCur] == 0:
            visit[nCur] = 1
            dq.append([nCur, count + 1, route + [nCur]])

            