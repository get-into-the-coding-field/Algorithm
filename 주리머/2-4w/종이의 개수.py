'''
백준 9375. 종이의 개수
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1
'''

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
answer = [0, 0, 0]



def dfs(x, y, n):
    
    mark = paper[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            
            if paper[i][j] != mark:
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * (n // 3), y + l * (n // 3), n // 3)
                return
    
    answer[mark+1] += 1
    return
    
dfs(0, 0, n)

for a in answer:
    print(a)