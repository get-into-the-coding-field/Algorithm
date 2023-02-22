import string

def solution(name):
    ascii = list(string.ascii_uppercase)
    ascii_length = len(ascii)
    answer = 0
    
    # 글자 수 변경 횟수 미리 저장
    name_move_sum = [min(ascii.index(n), ascii_length - ascii.index(n)) for n in name]
    answer += sum(name_move_sum)
    
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    for i in range(len(name)):
        
        next = i + 1
        
        while next < len(name) and name[next] == "A":
            next += 1
        # 요 식이 조금 까다로움
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])
        
    
    answer += min_move
    return answer

print(solution("JEROEN")) # 56
print(solution("JAN")) # 23
print(solution("AAAAABBAAAAAAABAAA")) # 16
print(solution("ABAAAAAAAAABB")) # 7
print(solution("AAB")) # 2
print(solution("AAABBBABAAB")) # # 13
