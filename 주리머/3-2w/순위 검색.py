import bisect
from collections import defaultdict
def solution(info, query):
    answer = []
    hash = defaultdict(list)
    
    for fo in info:
        infos = fo.split(" ")
        key = "".join([i[0] for i in infos[:-1]])
        hash[key].append(int(infos[-1]))
                            
        # print(f'infos: {infos}, hash: {hash}')
    for k in hash.keys():
        hash[k].sort()
    
    for q in query:
        cnt = 0
        qq = q.split(" and ")
        
        # 소울푸드와 점수 분리하여 추가
        qq += qq.pop().split(" ")
        
        queryKey = "".join([q[0] for q in qq[:-1]])
        score = int(qq[-1])
        # print(f'queryKey: {queryKey}, score: {score}')
        for targetKey in hash.keys():
            value = hash[targetKey]
            for i in range(4):
                if queryKey[i] == "-" or targetKey[i] == queryKey[i]:
                    continue
                break
            else:
                left = bisect.bisect_left(value, score)
                cnt += len(value) - left
        answer.append(cnt)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]               ))