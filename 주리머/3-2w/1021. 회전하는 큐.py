'''
백준 1021. 회전하는 큐
https://www.acmicpc.net/problem/1021

10 3
1 2 3

'''
from collections import deque

n, m = map(int, input().split())
arr = deque([i for i in range(1, n+1)])
target = list(map(int, input().split()))
cnt = 0


for t in target:
    while True:
        if arr[0] == t:
            arr.popleft()
            break
        else:
            if arr.index(t) <= len(arr) // 2:
                arr.append(arr.popleft())
                cnt += 1
            else:
                arr.appendleft(arr.pop())
                cnt += 1
print(cnt)