'''
다이나믹 롤러 (이분탐색)
https://www.acmicpc.net/problem/17393
'''

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
answer = []

for i in range(n):
    target = arr1[i]
    start = i
    end = 500000
    
    while start <= end:
        mid = (start + end) // 2
        
        if mid >= n:
            end = mid - 1
            continue
        
        if arr2[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    answer.append(end-i)
    
print(*answer)
        