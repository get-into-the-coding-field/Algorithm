'''
3*n 타일링
https://school.programmers.co.kr/learn/courses/30/lessons/12902
'''

def solution(n):
    answer = 0
    dp = [0] * (n + 1)
    dp[0] = 1
    MOD = 1000000007
    
    if n % 2 == 1:
        return 0
    
    for i in range(2, n + 1, 2):
        if i == 2:
            dp[i] = 3
            continue
        
        dp[i] = (((dp[i - 2] * 4) % MOD) - dp[i - 4]) % MOD 
    return dp[10]


print(solution(10))