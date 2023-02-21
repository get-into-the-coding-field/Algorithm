# n = int(input())
# costs = []

# for i in range(n):
#     costs.append(list(map(int, input().split())))
    
# dp = [[0] * 3 for i in range(n)]
# dp[0][0], dp[0][1], dp[0][2] = costs[0][0], costs[0][1], costs[0][2]

# for i in range(1, n):
#     dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
#     dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
#     dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])


# print(min(dp[n-1]))


def solution(elements):
    length = len(elements)
    elements = elements * 2
    result = set()
    
    for i in range(1, length + 1):
        for j in range(length):
            result.add(sum(elements[j:j+i]))
    
    return len(result)


# print(solution([7,9,1,1,4])) # 18


dp = []
# 30
# 26 40 83
# 49 60 57
# 13 89 99