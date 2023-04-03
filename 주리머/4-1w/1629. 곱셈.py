'''
백준 1629. 곱셈
https://www.acmicpc.net/problem/1629
'''


def solution():
    a, b, c = map(int, input().split())

    def power(a, b):
    
        if b == 1:
            return a % c
        else:
            tmp = power(a, b//2)
            if b % 2 == 0:
                return tmp * tmp % c
            else:
                return tmp * tmp * a % c
    return power(a, b)
print(solution())