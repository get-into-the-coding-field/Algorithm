from itertools import chain
def solution(n):
    answer = [[0] * (i+1) for i in range(n)]
    answer[0][0] = 1
    global count, i, j
    i = 0
    j = 0
    count = 2
    
    def ascending():
        global count, i, j
        
        for k in range(i+1, n):
            if answer[k][j] != 0:
                i = k - 1
                break
            
            if k == n-1:
                i = k
                
            answer[k][j] = count
            count += 1
            
    
    def descending():
        global count, i, j
        
        for k in range(i-1, -1, -1):
            if answer[k][j-1] != 0:
                i = k + 1
                break
            
            j -= 1
            answer[k][j] = count
            count += 1
            
    def inARow():
        global count, i, j
        
        for k in range(j+1, n):
            if answer[i][k] != 0:
                j = k - 1
                break
            
            if k == n-1:
                j = k

            answer[i][k] = count
            count += 1
            
    number = n
    while number > 0:
    
        ascending() 
        
        number -= 1
        if number == 0:
            break
        
        inARow()
        
        number -= 1
        if number == 0:
            break
        
        
        descending()
        
        number -= 1
        if number == 0:
            break

    return sum(answer, [])

print(solution(4))
print(solution(6))
print(solution(7))

# 초기 설정은 [[0] * (i+1) for i in range(n)]
# 내려올 땐 i에 +1 값으로(종료조건 삽입), 다 내려오면 그 줄에서 +1, 올라갈 땐 i-1에 +1씩 증가
# 종료조건은 0이 아니라면 종료