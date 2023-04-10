'''
백준 2263. 트리 순회
https://www.acmicpc.net/problem/2263
'''
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def pre_order(in_start, in_end, post_start, post_end):
    # 재귀 종료 조건
    if(in_start > in_end) or (post_start > post_end):
        return

    # 후위 순회 결과의 끝이 루트
    root = post_order[post_end]
    print(root, end=" ")

    
    left = position[root] - in_start
    right = in_end - position[root]

    # 왼쪽 서브 트리
    pre_order(in_start, in_start+left-1, post_start, post_start+left-1) # 쪽 서브트리
    
    # 오른쪽 서브 트리
    pre_order(in_end-right+1, in_end, post_end-right, post_end-1) # 오른쪽 서브트리

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

position = [0]*(n+1)
for i in range(n):
    position[in_order[i]] = i

pre_order(0, n-1, 0, n-1)