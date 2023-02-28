
'''
백준 1931. 회의실 배정
https://www.acmicpc.net/problem/1931

11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''

import heapq as hq
import sys
input = sys.stdin.readline
n = int(input())
meeting_room = []
start, end = 0, 1

for _ in range(n):
    s, e = map(int, input().split())
    
    hq.heappush(meeting_room, (s, e))
    

answer = []

for _ in range(n):
    time = hq.heappop(meeting_room)
        
    if not answer:
        answer.append(time)
    else:
        if answer[-1][end] > time[end]:
            answer.pop()
            answer.append(time)
            continue
        
        if answer[-1][end] <= time[start]:
            answer.append(time)
    
print(len(answer))
    
        