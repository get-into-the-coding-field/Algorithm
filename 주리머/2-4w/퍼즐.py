'''
백준 1525. 퍼즐
https://www.acmicpc.net/problem/1525

1 0 3
4 2 5
7 8 6

1 2 3
4 5 0
6 7 8

13

'''
from collections import deque
target = "123456789"
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
puzzle = ""
for _ in range(3):
    puzzle += "".join(list(input().split()))
puzzle = puzzle.replace("0", "9")

visited = {puzzle: 0}
    
def bfs():
    
    dq = deque([puzzle])
    
    while dq:
        pz = dq.popleft()
        cnt = visited[pz]
        z = pz.find("9")
        
        if pz == target:
            return cnt
        
        x = z // 3
        y = z % 3
        cnt += 1
        
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            
            if 0 <= nx < 3 and 0 <= ny < 3:
                nz = nx * 3 + ny
                puzzleList = list(pz)
                puzzleList[z], puzzleList[nz] = puzzleList[nz], puzzleList[z]
                newPuzzle = "".join(puzzleList)

                if newPuzzle not in visited:
                    visited[newPuzzle] = cnt
                    dq.append(newPuzzle)
    return -1

print(bfs())



