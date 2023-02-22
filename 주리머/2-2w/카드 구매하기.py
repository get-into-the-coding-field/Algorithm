n = int(input())
cards = list(map(int, input().split()))
cards.insert(0, 0)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], cards[j] + dp[i-j])

print(dp)
print(dp[n])

# 아이디어 참고 블로그!
# [[Python] 백준 11052번: 카드 구매하기 풀이](https://jyeonnyang2.tistory.com/56)
