'''
백준 2578. 빙고
https://www.acmicpc.net/problem/2578
'''
bingo = []

for _ in range(5):
    bingo.append(list(map(int, input().split())))    

call_count = 0
draw = [[0] * 5 for _ in range(5)]


def check_if_bingo(arr):
    x, y = arr
    
    # 해당 좌표의 가로, 세로, 대각선 확인
    bingoCount = 0
    for i in range(5):
        if draw[i].count(1) == 5:
            bingoCount += 1
        
    for i in range(5):
        count = 0
        for j in range(5):
            if draw[j][i] == 1:
                count += 1
            else:
                break
        
        if count == 5:
            bingoCount += 1
    
    count = 0
    for i in range(5):
        if draw[i][i] == 1:
            count += 1
    
    if count == 5:
        bingoCount += 1
        
    count = 0
    
    for i in range(5):
        if draw[i][4-i] == 1:
            count += 1
    
    if count == 5:
        bingoCount += 1
    
    if bingoCount >= 3:
        return True

def check(n):    
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == n:
                draw[i][j] = 1
                return [i, j]
            
for _ in range(5):
    call = list(map(int, input().split()))
    isComplete = False
    
    for c in call:
        coordinate = check(c)
        call_count += 1
        # 빙고 3줄의 최소값 = 12개
        if call_count >= 10:
            if check_if_bingo(coordinate):
                isComplete = True
                break
    if isComplete:
        break

print(call_count)