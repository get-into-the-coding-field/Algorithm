
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
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    wear = []
    for _ in range(n):
        a, b = input().split()
        wear.append(b)

    wear_Counter = Counter(wear)
    
    print(f'wear_Counter: {wear_Counter}')
    cnt = 1 # 각 종류마다 항목의 개수

    for key in wear_Counter:
        cnt *= wear_Counter[key] + 1

    print(cnt-1)
        
    