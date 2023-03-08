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
# 10, 12 ,3 , 9
def calculate(m, n, x, y):
    k = x #k를 x로 초기화
    
    while k <= m * n: #k의 범위는 m*n을 넘을 수 없기에
        # print(f'k: {k}, x: {x}, y: {y}, m: {m}, n: {n}')
        if (k - x) % m == 0 and (k - y) % n == 0: #2개의 조건을 만족하는 k값을 찾는다.
            return k
        k += m #k-x가 m의 배수이기 때문에 k는 x로 초기화해주었기 때문에 m만 더해준다.
    return -1

for _ in range(n):
    N, M, x, y = map(int, input().split())
    countX = 1
    countY = 1
    year = 1
    
    
    print(calculate(N, M, x, y))
