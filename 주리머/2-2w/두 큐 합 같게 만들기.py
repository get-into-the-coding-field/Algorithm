from collections import deque

def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)
    
    if total % 2 == 1:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = len(queue1) * 3
    total1 = sum(queue1)
    total2 = sum(queue2)
    answer = 0
    
    while True:
        if total1 > total2:
            a = queue1.popleft()
            queue2.append(a)
            total2 += a
            total1 -= a
            answer += 1
        elif total2 > total1:
            b = queue2.popleft()
            queue1.append(b)
            total1 += b
            total2 -= b
            answer += 1
        else:
            break

        if answer >= limit:
            answer = -1
            break
    return answer

print(solution([3, 2, 7, 2],[4, 6, 5, 1]))
print(solution([1, 2, 1, 2],[1, 10, 1, 2]))
print(solution([1, 1],[1, 5]))
# 3272  = 14
# 4651  = 16