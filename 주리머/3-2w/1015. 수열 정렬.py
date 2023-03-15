'''
백준 1015. 수열 정렬

3
2 3 1

'''

n = int(input())
arr = [i for i in range(n)]
seq = list(map(int, input().split()))
seq_asc = sorted(seq)
answer = []

for s in seq:
    idx = seq_asc.index(s)
    seq_asc[idx] = -1
    answer.append(arr[idx])

print(*answer)
