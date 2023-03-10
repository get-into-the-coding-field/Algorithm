'''
백준 9375. 패션왕 신해빈
https://www.acmicpc.net/problem/9375

2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face

'''

import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    hash = defaultdict(int)
    n = int(input())
    
    for _ in range(n):
        wear, sort = input().strip().split()
        hash[sort] += 1
        
    result = 1
    for val in hash.values():
        result *= (val + 1)
    
    print(result - 1)
    
    
    