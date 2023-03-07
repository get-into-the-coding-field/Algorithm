'''
백준 6064. 카잉 달력
https://www.acmicpc.net/problem/6064

3
10 12 3 9
10 12 7 2
13 11 5 6

1
10 12 3 9
'''

#  x < M 이면 x' = x + 1이고, 그렇지 않으면 x' = 1이다. 
# 같은 방식으로 만일 y < N이면 y' = y + 1이고, 그렇지 않으면 y' = 1

# 1. x, y를 1씩 증가시키면서 M, N이 되면 종료

n = int(input())

for _ in range(n):
    N, M, x, y = map(int, input().split())
    countX = 1
    countY = 1
    year = 1
    
    while True:
        # print(f'{year}번째 해: {countX}, {countY}')
        if countX == x and countY == y:
            break
        
        if countX == N and countY == M:
            year = -1
            break
        
        if countX < N:
            countX += 1
        else:
            countX = 1
        
        if countY < M:
            countY += 1
        else:
            countY = 1
        
        year += 1
    print(year)
