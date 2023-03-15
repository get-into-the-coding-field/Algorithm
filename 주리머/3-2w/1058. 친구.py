'''
백준 1058. 친구
https://www.acmicpc.net/problem/1058

3
NYY
YNY
YYN

'''

# 친구와 친구의친구 수가 가장 많은 사람
from collections import deque
n = int(input())
result = [0] * n
friends = [list(input().strip()) for _ in range(n)]
relation = [[0] * n for _ in range(n)]

dq = deque([])
for i in range(n):
    dq.append((i, i, 0))

while dq:
    # 친구의 시작점, 확인해 볼 친구
    start, target, cnt = dq.popleft()
    
    # print(f'start: {start}, target: {target}')
    for i, friend in enumerate(friends[target]):
        # print(f'i: {i}, friend: {friend}')
        if start != i and friend == 'Y' and relation[start][i] == 0:
            result[start] += 1
            relation[start][i] = 1
            
            if cnt < 1:
                dq.append((start, i, cnt + 1))

print(max(result))
            
            