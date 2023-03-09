'''
백준 10819. 차이를 최대로
https://www.acmicpc.net/problem/10819
'''


n = int(input())
from itertools import permutations
answer = 0
arr = list(map(int, input().split()))
combi = list(permutations(arr, n))

def bt(tmp, total, cnt, visited):
    if cnt == n:
        global answer
        answer = max(answer, total)
        return
    
    for i in range(n):
        if i not in visited:
            visited.append(i)
            bt(tmp + [arr[i]], total + abs(tmp[-1]-arr[i]), cnt + 1, visited)
            visited.pop()

for i in range(n):
    bt([arr[i]], 0, 1, [i])
print(answer)
# for i in range(1, n):