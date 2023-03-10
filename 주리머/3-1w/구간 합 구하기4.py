'''
백준 11659. 구간 합 구하기4.py
https://www.acmicpc.net/problem/11659

5 3
5 4 3 2 1
1 3
2 4
5 5

'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]

tot = 0
for i in range(n):
    tot += arr[i]
    prefix_sum.append(tot)    

for _ in range(m):
    i, j = map(int, input().split())    
    print(prefix_sum[j] - prefix_sum[i-1])

