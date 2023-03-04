'''
백준 11724. 연결 요소의 개수
https://www.acmicpc.net/problem/11724

6 5
1 2
2 5
5 1
3 4
4 6

'''

n, m = map(int, input().split())
maps = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)

visit = [0] * (n + 1)

def dfs(i):
    count = 0
    
    
    for j in maps[i]:
        if visit[j] == 0:
            # 방문 처리 및 count 처리
            visit[j] = 1
            count += 1 + dfs(j)
    
    return count
            
            

answer = 0
for i in range(1, n + 1):
    if len(maps[i]) > 0:
        visit[i] = 1
        if dfs(i) > 0:
            answer += 1
# 방문처리 되지 않은 노드를 더해준다.
# print(visit)
print(answer + visit[1:].count(0))