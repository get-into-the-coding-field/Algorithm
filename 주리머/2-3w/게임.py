import math
n, m = map(int, input().split())
z = m * 100 // n 

if z >= 99:
    print(-1)
else:
    
    answer = n
    start = 1
    end = n * 2
    
    while start <= end:
        mid = (start + end) // 2
        
        if int(((m + mid) / (mid + n) * 100)) > z:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    
    print(answer)
            
