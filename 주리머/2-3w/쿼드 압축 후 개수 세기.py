def conquer(arr):
    length = len(arr)
    # 더 이상 분할할 수 없을 떄
    if length < 2:
        answer[arr[0][0]] += 1
        return
    
    # 분할할 수 있을 때
    previous = arr[0][0]
    for i in range(length):
        for j in range(length):
            if arr[i][j] != previous:
                conquer([row[:length//2] for row in arr[:length//2]])
                conquer([row[length//2:] for row in arr[:length//2]])
                conquer([row[:length//2] for row in arr[length//2:]])
                conquer([row[length//2:] for row in arr[length//2:]])
                return
            
    answer[previous] += 1
    
def solution(arr):
    global answer
    answer = [0, 0]
    

    conquer(arr)
    return answer

# 
print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
