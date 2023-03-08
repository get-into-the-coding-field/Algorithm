'''


4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]

'''

import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    order = list(input().strip())
    n = int(input())
    arrInput = input()
    arr = deque([])
    
    if n != 0:
        arr = deque([i for i in arrInput[1:-2].split(",")])
    
    rCount = 0
    isError = False
    
    for o in order:
        if o == "R":
            rCount += 1
        else:
            if len(arr) == 0:
                isError = True
                print("error")
                break
            
            if rCount % 2 == 1:
                arr.pop()
            else:
                arr.popleft()

        
    if not isError:
        if len(arr) == 0:
            print("[]")
        else:
            if rCount % 2 == 1:
                arr.reverse()
            print("[" + ",".join(arr) + "]")