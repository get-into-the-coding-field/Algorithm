n = int(input())
chess = [0] * n
answer = 0

def canPut(y):
    
    for i in range(y):
        if chess[y] == chess[i] or abs(chess[y] - chess[i]) == abs(y - i):
            return False
    return True

def playChess(y):
    if y == n:
        global answer
        answer += 1
        return
    
    for i in range(n):
        chess[y] = i
        if canPut(y):
            playChess(y + 1)

playChess(0)
print(answer)