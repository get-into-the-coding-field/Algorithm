'''
백준 1062. 가르침
https://www.acmicpc.net/problem/1062

3 6
antarctica
antahellotica
antacartica

antic 5개는 기본적으로..!
'''
from collections import defaultdict
from itertools import combinations
import string
n, k = map(int, input().split())

if k < 5:
    for i in range(n):
        input()
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()

combi = [["a", "n", "t", "i", "c"] + [*c] for c in list(combinations([s for s in string.ascii_lowercase if s not in ["a", "n", "t", "i", "c"]], k-5))]
# print(combi)
answer = 0
words = [input() for _ in range(n)]
for c in combi:
    cnt = 0
    for word in words:
        for w in word:
            if w not in c:
                break
        else:
            cnt += 1
    answer = max(answer, cnt)
print(answer)