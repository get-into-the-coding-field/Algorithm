def solution(skill, skill_trees):
    answer = 0
    
    for user_skill in skill_trees:
        remainSkill = "".join([s for s in user_skill if s in skill])
        isSame = True
        
        for i in range(len(remainSkill)):
            if remainSkill[i] != skill[i]:
                isSame = False
                break
        if isSame:
            answer += 1

    return answer
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))