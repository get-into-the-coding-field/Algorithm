def solution(elements):
    length = len(elements)
    elements = elements * 2
    result = set()
    
    for i in range(1, length + 1):
        for j in range(length):
            result.add(sum(elements[j:j+i]))
    
    return len(result)


print(solution([7,9,1,1,4])) # 18




