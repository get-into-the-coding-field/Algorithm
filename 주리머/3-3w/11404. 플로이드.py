'''
백준 11404. 플로이드
https://www.acmicpc.net/problem/11404
'''

n = int(input())
m = int(input())
INF = int(1e9)
arr = [[INF] * (n) for _ in range(n)]

for _ in range(m):
    s, e, t = map(int, input().split())
    arr[s-1][e-1] = min(arr[s-1][e-1], t)

# 플로이드 와샬 알고리즘
def floydWarshall():
    global arr
    # 거쳐가는 노드
    for k in range(n):
        # 출발 노드
        for i in range(n):
            if i == k:
                continue
            # 도착 노드
            for j in range(n):
                if j == k:
                    continue
                if i != j:
                    if arr[i][j] > arr[i][k] + arr[k][j]:
                        arr[i][j] = arr[i][k] + arr[k][j]
floydWarshall()

for i in range(n):
    # 도착하지 못할 경우(무한) 0처리 
    print(*[0 if a == INF else a for a in arr[i]])