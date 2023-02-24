def solution(keymap, targets):
    answer = []
    
    for i in range(len(targets)):
        sum = 0
        for j in range(len(targets[i])):
            findTarget = targets[i][j]
            
            minIdx = int(1001)
            for k in range(len(keymap)):
                a = 1001 if keymap[k].find(findTarget) == -1 else keymap[k].find(findTarget)
                minIdx = min(minIdx, a)
                
            # print(f'k: {k}, minIdx: {minIdx}, findTarget: {findTarget}, keymap[k]: {keymap[k]}')                
            if minIdx != 1001:
                sum += minIdx + 1
        
        if sum != 0:
            answer.append(sum)
        else:
            answer.append(-1)                
    return answer

print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))
print(solution(["AA"],["B"]))
print(solution(["AGZ", "BSSS"],["ASA","BGZ"]))
