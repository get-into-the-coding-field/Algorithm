'''
백준 4108. 지뢰찾기
https://www.acmicpc.net/problem/4108
'''

while True:
    r, c = map(int, input().split())
    maps = []
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    answer = []
    
    if r == 0 and c == 0:
        break
    
    for _ in range(r):
        maps.append(list(input().strip()))
    
    def detectMine(x, y):
        cnt = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c:
                if maps[nx][ny] == '*':
                    cnt += 1
        return str(cnt)
        
    
    for i in range(r):
        tmp = []
        for j in range(c):
            if maps[i][j] == "*":
                tmp.append("*")
            else:
                tmp.append(detectMine(i, j))
        answer.append("".join(tmp))
    
    for a in answer:
        print(a)
    
    
    