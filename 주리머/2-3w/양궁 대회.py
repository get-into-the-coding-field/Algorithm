import sys
sys.setrecursionlimit(10**6)

def solution(n, info):
    global answer
    global maxDiff
    answer = []
    maxDiff = 0
    
    
    def backtracking(target, arr, arrow, total):
        global answer
        global maxDiff
        
        if arrow == 0 or target == 10:
            if sum(arr) != total:
                print(arr)
                return
            
            aScore = 0
            bScore = 0
            
            for i in range(11):
                if arr[i] == 0 and info[i] == 0:
                    continue
                elif arr[i] > info[i]:
                    bScore += (10 - i)
                else:
                    aScore += (10 - i)

            if bScore > aScore:
                if bScore - aScore > maxDiff:
                    maxDiff = bScore - aScore
                    answer.clear()
                    answer.append((bScore-aScore, *arr))
                elif bScore - aScore == maxDiff:
                    answer.append((bScore-aScore, *arr))
            return
        
        
        # 과녁을 안쏘는 경우
        backtracking(target+1, arr, arrow, total)
        
        # 과녁을 쏘는 경우
        if target + 1 == 10:
            if arrow > 0: # 마지막에 화살이 남았을 경우 다 쏜다
                tmp = arr[target + 1]
                arr[target + 1] = arrow
                arrow = 0
                backtracking(target + 1, arr, arrow, total)
                arr[target + 1] -= tmp
                arrow = arr[target + 1]
        else:
            if arrow >= (info[target+1] + 1):
                arr[target+1] += (info[target+1] + 1)
                arrow -= (info[target+1] + 1)
                backtracking(target+1, arr, arrow, total)
                arrow += (info[target+1] + 1)
                arr[target+1] -= (info[target+1] + 1)
                

        
    for i in range(11):
        tmp = [0] * 11
        arrow = n
        
        # 과녁을 안 쏘는 경우
        backtracking(i, tmp, arrow, n)
        # 과녁을 쏘는 경우
        tmp[i] += (info[i] + 1)
        arrow -= (info[i] + 1)
        backtracking(i, tmp, arrow, n)
        tmp[i] -= (info[i] + 1)
        arrow += (info[i] + 1)
        
    print(answer)
    
    if len(answer) > 0:
        return list(sorted([i for i in answer if i[0] == maxDiff])[0][1:])
    else:
        return [-1]
    
# print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))