'''백준
팩토리얼 0의 개수
'''

dp = [0] * 501

dp[0], dp[1] = 0, 1
n = int(input())


for i in range(2, n + 1):
    dp[i] = dp[i-1] * i
    

count = 0

for i in range(len(str(dp[n])) -1, -1, -1):
    if n == 0:
        break
    
    if str(dp[n])[i] != "0":
        break
    
    count += 1
    
print(count)
    
