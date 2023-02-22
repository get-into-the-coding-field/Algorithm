def hanoi(n, start, end, assist):
    global answer
    if n == 1:
        answer.append([start, end])
        return
    
    hanoi(n-1, start, assist, end)
    answer.append([start, end])
    hanoi(n-1, assist, end, start)
    
def solution(n):
    global answer
    answer = []
    
    hanoi(n, 1, 3, 2)
    return answer

print(solution(2))
print(solution(5))
print(solution(15))