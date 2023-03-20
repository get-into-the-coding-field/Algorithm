def solution(gems):
    sort = set(gems)
    start = 0
    end = 0
    length = len(gems)
    count_set = set()
    count_dict = {}
    answer = [1e9, 0, 0]
    while start < length and end < length:
        # end 윈도우 늘림
        while len(count_set) < len(sort) and end < length:
            if gems[end] in count_dict:
                count_dict[gems[end]] += 1
            else:
                count_dict[gems[end]] = 1
                count_set.add(gems[end])
            end += 1
        
        # start 윈도우 늘림
        while len(count_set) == len(sort) and start < length:
            if answer[0] > end - start:
                answer = [end - start, start+1, end]
                
            if gems[start] in count_dict:
                count_dict[gems[start]] -= 1
                if count_dict[gems[start]] == 0:
                    count_set.remove(gems[start])
                    del count_dict[gems[start]]
            start += 1
        
            
    return answer[1:]

print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))