import sys
input = sys.stdin.readline
n = int(input())
triangles = []
dp = [[0] * (i + 1) for i in range(n)]

for i in range(n):
    triangles.append(list(map(int, input().split())))

dp[0][0] = triangles[0][0]

# print(f'dp: {dp}')
# print(f'triangles: {triangles}')

for i in range(1 , n):
    for j in range(i + 1):
        
        # 0과 끝은 하나만 더해주면 됨
        # 나머지는 max값을 넣어줌
        # print(i, j)
        if j == 0:
            # print(f'i: {i} j: {j}, 값: {dp[i-1][0]} + {triangles[i][j]}')
            dp[i][j] = dp[i-1][0] + triangles[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangles[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangles[i][j]
    
# print(triangles)
# print(dp)
print(max(dp[n-1]))