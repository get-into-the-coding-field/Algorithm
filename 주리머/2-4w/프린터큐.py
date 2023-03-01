'''
백준 1966. 프린터큐
https://www.acmicpc.net/problem/1966

3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

'''


import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, targetIdx = map(int, input().split())
    q = list(map(int, input().split()))
    idxQueue = list(range(len(q)))
    idxQueue[targetIdx] = "요놈이다"
    answer = 0
    
    while True:
        maxValue = max(q)
        
        if q[0] == maxValue:
            if idxQueue[0] == "요놈이다":
                answer += 1
                break
            else:
                q.pop(0)
                idxQueue.pop(0)
                answer += 1
        else:
            q.append(q.pop(0))
            idxQueue.append(idxQueue.pop(0))    
            
            
        
    print(answer)
    
'''
1
4 1
2 1 3 1


'''    
        
    
    
    


