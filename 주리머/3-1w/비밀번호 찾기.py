'''
백준 17219. 비밀번호 찾기
https://www.acmicpc.net/problem/17219
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cash = {}
for _ in range(n):
    site, password = input().strip().split()
    cash[site] = password
    
for _ in range(m):
    site = input().strip()
    print(cash[site])

