
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    for i in range(a + 1):                
        for j in range(b + 1):
            for k in range(c + 1):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 1
                elif i < j < k:
                    dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
                else:
                    dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]
    return dp[a][b][c]
    

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')



    '''    
    1 1 1
    2 2 2
    10 4 6
    50 50 50
    -1 7 18
    -1 -1 -1
    '''