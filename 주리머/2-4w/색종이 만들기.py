'''
백준 2630. 색종이 만들기
https://www.acmicpc.net/problem/2630

8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
'''

n = int(input())
arr = []
answer = [0, 0]

for i in range(n):
    arr.append(list(map(int, input().split())))

def divideConquer(arr):
    if len(arr) == 1:
        answer[arr[0][0]] += 1
        return 
    
    mark = arr[0][0]

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != mark:
                divideConquer([row[:len(arr)//2] for row in arr[:len(arr)//2]])
                divideConquer([row[:len(arr)//2] for row in arr[len(arr)//2:]])
                divideConquer([row[len(arr)//2:] for row in arr[:len(arr)//2]])
                divideConquer([row[len(arr)//2:] for row in arr[len(arr)//2:]])
                return
    
    answer[mark] += 1      
    return
    

divideConquer(arr)    
print(answer[0])
print(answer[1])

