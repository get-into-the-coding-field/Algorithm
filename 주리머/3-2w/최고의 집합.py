'''

'''

def solution(n, s):    
    answer = []
    while len(answer) < n:
        if len(answer) == n - 1:
            answer.append(s)
            break
        quota = s // (n - len(answer))
        if quota == 0:
            answer = [-1]
            break
        s -= quota
        answer.append(quota)
        
    return answer

print(solution(3, 15))
print(solution(2, 1))
# print(solution(2, 8))
# print(solution(4, 1000))
