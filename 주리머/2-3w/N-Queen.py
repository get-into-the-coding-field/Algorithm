
            
def solution(n):
    answer = 0
    chess = [0] * n
    
    def check(x):
        for i in range(x):
            if chess[i] == chess[x] or abs(chess[x] - chess[i]) == abs(x - i):
                return False
        return True

    def put_queen(x):
        count = 0
        if x == n:
            return 1
        
        for i in range(n):
            chess[x] = i
            if check(x):
                count += put_queen(x + 1)
            else:
                continue
        return count
            
    answer += put_queen(0)
    
    return answer

print(solution(12))