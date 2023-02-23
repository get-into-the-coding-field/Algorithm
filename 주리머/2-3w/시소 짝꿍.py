from collections import defaultdict
def solution(weights):
    answer = 0
    weightDict = defaultdict(int)
    
    for w in weights:
        answer = answer + weightDict[w] + weightDict[(w*2)] + weightDict[(w/2)] + weightDict[((w*2)/3)] + weightDict[((w*3)/2)] + weightDict[((w*3)/4)] + weightDict[((w*4)/3)]
        weightDict[w] += 1
    
    return answer

print(solution([100,180,360,100,270]))