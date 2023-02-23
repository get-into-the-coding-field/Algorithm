'''
점 찍기
좌표평면에 점끼리의 거리를 계산 할 수 있어야함 x^2 + y^2 = d^2
https://school.programmers.co.kr/learn/courses/30/lessons/140107
'''

import math
def solution(k, d):
    answer = 0
    yLimit = d * d
    for i in range(0, d + 1, k):
        xLimit = i * i
        res_d = math.floor(math.sqrt(yLimit-xLimit))
        answer += (res_d//k) + 1
    return answer

