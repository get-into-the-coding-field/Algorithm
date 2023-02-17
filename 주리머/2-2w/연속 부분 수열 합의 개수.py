def solution(elements):
    answer = set()
    length = len(elements)
    
    for i in elements:
        answer.add(i)
        
    totalSum = sum(elements)
    answer.add(totalSum)

    elements = elements * 2
    
    for limitLength in range(2, length):
        for startIdx in range(length):
            answer.add(sum(elements[startIdx:startIdx+limitLength]))

    return len(answer)

print(solution([7,9,1,1,4]))

