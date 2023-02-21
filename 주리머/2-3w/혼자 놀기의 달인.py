'''
혼자 놀기의 달인
https://school.programmers.co.kr/learn/courses/30/lessons/131130
'''

def solution(cards):
    answer = []
    used = [False] * (len(cards) + 1)
    
    for idx, c in enumerate(cards):
        
        if used[idx + 1]:
            continue
        
        used[idx + 1] = True
        tmpBox = [idx + 1]
        
        while True:
            if not used[c]:
                used[c] = True
                tmpBox.append(c)
                c = cards[c-1]
            else:
                break
            
        if len(tmpBox) > 0:
            answer.append(len(tmpBox))
                
    answer.sort()
    
    if len(answer) > 1: 
        return answer[-1] * answer[-2]
    else:
        return 0


print(solution([8,6,3,7,2,5,1,4]))

# [8,6,3,7,2,5,1,4] -> 12