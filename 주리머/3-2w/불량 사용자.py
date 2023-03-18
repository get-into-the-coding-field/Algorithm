import re
import itertools
import collections
def solution(user_id, banned_id):
    # 정규식으로 구하고
    # 조합으로 값 구하기
    answer = []
    combination = []
    
    for ban_id in banned_id:
        combi = []
        for id in user_id:
            if re.match(ban_id.replace("*", ".{1}")+"$", id):
                combi.append(id)
                # print(f'ban_id : {ban_id}, id: {id}')
        combination.append(combi)
    length = len(combination)
    dq = collections.deque([([], 0)])
    
    while dq:
        arr, c = dq.popleft()
        
        if len(arr) == length:
            # print(f'완성된 불량사용자 리스트:  {arr}')
            arr.sort()
            if arr not in answer:
                answer.append(arr)
            continue
        
        # print(f'arr: {arr}, c: {c}')
        for combi in combination[c]:
            if combi not in arr:
                dq.append((arr + [combi], c + 1))
            
    return len(answer)
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))