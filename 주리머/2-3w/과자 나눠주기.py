'''
백준 16401. 과자 나눠주기
https://www.acmicpc.net/problem/16401
'''
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    
    if mid == 0:
        result = 0
        break
    
    for x in arr:
        if x >= mid:
            total += (x // mid)
    
    if total >= n:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)