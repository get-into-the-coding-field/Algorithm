'''
프로그래머스 lv3. 풍선 터트리기
https://school.programmers.co.kr/learn/courses/30/lessons/68646
'''

def solution(a):
    result = [False for _ in range(len(a))]
    min_left, min_right = float("-inf"), float("-inf")
    
    for i in range(len(a)):
        # 0부터 시작해서 배열의 마지막까지 최소값인 배열의 index True로 갱신한다.
        if a[i] < min_left:
            min_left = a[i]
            result[i] = True
        # 배열의 마지막부터 시작해서 0까지 최소값인 배열의 index를 True로 갱신한다.
        if a[-1-i] < min_right:
            min_right = a[-1-i]
            result[-1-i] = True
    return sum(result)

print(solution([9, -1, -5]))