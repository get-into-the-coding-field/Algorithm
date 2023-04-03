'''
프로그래머스 lv3. 합승 택시 요금
https://school.programmers.co.kr/learn/courses/30/lessons/72413
'''

def solution(n, s, a, b, fares):
    def floyd():
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if i == j:
                        edges[i][j] = 0
                        continue
                        
                    if edges[i][j] > edges[i][k] + edges[k][j]:
                        edges[i][j] = edges[i][k] + edges[k][j]
    INF = int(1e9)
    edges = [[INF] * (n+1) for _ in range(n+1)]
    answer = INF
    
    for start, end, cost in fares:
        edges[start][end] = cost
        edges[end][start] = cost
    
    floyd()
    
    for m in range(1, n+1):
        answer = min(edges[s][m] + edges[m][a] + edges[m][b], answer)
    
    return answer