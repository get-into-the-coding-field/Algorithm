def solution(stones, k):
    answer = 0
    length = len(stones)
    
    left = 1
    right = 200000000
    
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for i in range(length):
            if stones[i] - mid <= 0:
                count += 1
            else:
                count = 0
            
            if count >= k:
                break
        if count >= k:
            right = mid - 1
        else:
            left = mid + 1
            answer = left
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3)) 
print(solution([7, 2, 8, 7, 5, 2, 9], 3))
print(solution([5, 7, 4, 3, 1, 2, 1], 3))