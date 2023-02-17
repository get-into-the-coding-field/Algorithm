
def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    global answer
    answer = 0
    direction = [(1, 0), (1, 1), (0, 1)]
    
    # 4개를 찾아서 삭제한다.
    # 삭제한 뒤에 빈 공간을 채운다.
    def move():
        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j] == '':
                        moved += 1
                        board[i+1][j] = board[i][j]
                        board[i][j] = ''
            if moved == 0:
                break
    
    def eraseTarget(arr):
        global answer
        
        for (i,j) in arr:
            answer += 1
            board[i][j] = ''                 
        return answer
    
    while True:
        targetToErase = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]  == '':
                    continue
                
                isTargetToErase = True
                tmp = [(i, j)]
                
                for (nx, ny) in direction:
                    dx = i + nx
                    dy = j + ny
                    
                    if board[i][j] != board[dx][dy]:
                        isTargetToErase = False
                        break
                    
                    tmp.append((dx, dy))
                    
                if isTargetToErase and len(tmp) > 0:
                    for t in tmp:
                        targetToErase.add(t)    
        
        if len(targetToErase) > 0:
            eraseTarget(targetToErase)
            move()
        else:
            break

    return answer

                
    
    
    

# print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(5, 6, ["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"]))
# print(solution(3,3,["JJA", "JJA", "JJA"]))