'''
백준 12865. 평범한 배낭
https://www.acmicpc.net/problem/12865
'''

'''
0-1 냅색 문제 ## 참고
https://claude-u.tistory.com/208
'''

n, k = map(int, input().split())
items = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
d = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = items[i][0]
        v = items[i][1] 
        # 해당 item의 무게가 j(index)보다 크면 이전 item의 가치를 가져온다.
        if j < w:   
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w] + v)
print(d[n][k])
    