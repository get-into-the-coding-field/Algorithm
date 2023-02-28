'''
백준 1927. 최소 힙
https://www.acmicpc.net/problem/1927

9
0
12345678
1
2
0
0
0
0
32

'''
import sys
import heapq as hq
input = sys.stdin.readline
arr = []

for i in range(int(input())):
    n = int(input())
    
    if n == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(hq.heappop(arr))
    else:
        hq.heappush(arr, n)    