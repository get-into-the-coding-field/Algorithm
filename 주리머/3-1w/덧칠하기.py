'''
프로그래머스 Lv2. 덧칠하기
https://school.programmers.co.kr/learn/courses/30/lessons/161989
'''

def solution(n, m, section):
    answer = 0
    section.sort()
    idx = 0
    color_distance = 0
    
    while idx < len(section):
        # print(f'idx: {idx}, color_distance: {color_distance}, answer: {answer}')
        if section[idx] > color_distance:
            color_distance = section[idx] + m - 1
            idx += 1
            answer += 1
            continue
        
        idx += 1
    return answer

print(solution(8, 4, [2, 3, 6]))
print(solution(5,4,[1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))