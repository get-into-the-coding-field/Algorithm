'''
백준 2407. 조합
https://www.acmicpc.net/problem/2407
'''

'''
nCm의 공식은 n! / (m! * (n-m)!)
'''
import sys
from fractions import Fraction
input = sys.stdin.readline
fac_arr = [0, 1]

def factorial():
    for i in range(2, 101):
        fac_arr.append(fac_arr[i-1] * i)

def solution():
    n, m = map(int, input().split())
    # Fraction으로 유리수 계산
    return Fraction(fac_arr[n], (fac_arr[m] * fac_arr[n-m]))
    
factorial()
print(solution())