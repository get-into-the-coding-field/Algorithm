def solution(numbers):
    answer = [0] * len(numbers)
    
    indexStack = []
    valueStack = []
    
    for idx, val in enumerate(numbers):
        if idx == 0:
            indexStack.append(idx)
            valueStack.append(val)
        else:
            if val > valueStack[-1]:
                while valueStack and val > valueStack[-1]:
                    answer[indexStack.pop()] = val
                    valueStack.pop()
            indexStack.append(idx)
            valueStack.append(val)
    
    while indexStack:
        answer[indexStack.pop()] = -1

    return answer
    
    # stack 2개
    # result 미리 만들어놓기

print(solution([2, 3, 3, 5])) # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2])) # [-1, 5, 6, 6, -1, -1]

# -1 5 5 3
# -1 -1 6 6 5 5 -1