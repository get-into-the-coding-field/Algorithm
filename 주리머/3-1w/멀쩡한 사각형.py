'''
프로그래머스 lv2. 멀쩡한 사각형
https://school.programmers.co.kr/learn/courses/30/lessons/62048
'''

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def solution(w,h):
    return (w * h) - (w + h - gcd(w, h))
