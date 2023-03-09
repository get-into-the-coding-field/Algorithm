'''
백준 9019 DSLR
https://www.acmicpc.net/problem/9019

3
1234 3412
1000 1
1 16

'''
import sys
from collections import deque
input = sys.stdin.readline

def calculate(num, dslr):
    if dslr == "D":
        return (num * 2) % 10000
    
    elif dslr == "S":
        return num - 1 if num != 0 else 9999
    
    elif dslr == "L":
        front = num % 1000
        back = num // 1000
        return front * 10 + back

    elif dslr == "R":
        front = num % 10
        back = num // 10
        return front * 1000 + back

for _ in range(int(input())):
    visit = [0] * 10000
    a, b = map(int, input().split())
    dslr = ["D", "S", "L", "R"]
    
    def bfs():
        
        dq = deque([])
        dq.append((a, ""))
        visit[a] = 1
        
        while dq:
            num, order = dq.popleft()
            
            for i in range(4):
                result = calculate(num, dslr[i])
                
                # print(f'num: {num}, dslr: {dslr[i]}, order: {order+dslr[i]}, result: {result}')
                if result == b:
                    return order + dslr[i]
                
                if visit[result] == 0:
                    visit[result] = 1
                    dq.append((result, order + dslr[i]))
    print(bfs())
        