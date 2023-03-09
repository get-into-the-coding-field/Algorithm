def hitleft(i):
    x = dom[i][0] - dom[i][1]
    for j in range(i-1, -1, -1):
        if dom[j][0] < x: return j+1
        x = min(x, dom[j][0] - dom[j][1])
    return 0

def hitright(i):
    x = dom[i][0] + dom[i][1]
    for j in range(i+1, n):
        if dom[j][0] > x: return j-1
        x = max(x, dom[j][0] + dom[j][1])
    return n-1

n = int(input())
dom = sorted(tuple(map(int,input().split())) for i in range(n))

print(f'dom: {dom}')
L = [hitleft(i) for i in range(n)]
R = [hitright(i) for i in range(n)]

dp = [10**9]*n + [0] # leftmost domino is i-th
for i in range(n-1, -1, -1):
    # hit i right
    dp[i] = 1 + dp[R[i]+1]
    # hit j left, s.t L[j] <= i
    for j in range(i+1, n):
        if L[j] <= i: dp[i] = min(dp[i], 1 + dp[j+1])
print(dp[0])