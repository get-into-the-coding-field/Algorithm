import sys
input = sys.stdin.readline

n, m = map(int, input().split())
video = list(map(int, input().split()))


start = 0
end = 1e10
answer = sum(video)

while start <= end:
    mid = (start + end) // 2
    
    if mid < max(video):
        start = mid + 1
        continue
    
    cnt, sum = 1, 0
    for i in range(len(video)):
        
        if video[i] + sum <= mid:
            sum += video[i]
        else:
            cnt += 1
            sum = video[i]
    
    if cnt <= m:
        answer = min(answer, mid)
        end = mid - 1
    else:
        start = mid + 1

print(int(answer))