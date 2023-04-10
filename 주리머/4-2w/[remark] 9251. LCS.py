'''
백준 9251. LCS
https://www.acmicpc.net/problem/9251
'''
import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()
word_length1 = len(word1)
word_length2 = len(word2)

dp = [[0] * (word_length2+1) for _ in range(word_length1+1)]

for i in range(1, word_length1+1):
    for j in range(1, word_length2+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])



    #     A C A Y K P
    # C   0
    # A   1
    # P   1
    # C
    # A
    # K
    