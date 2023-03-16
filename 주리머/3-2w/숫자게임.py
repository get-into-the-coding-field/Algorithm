# 첫번째 풀이
import bisect
from collections import deque
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    A = deque(A)
    B = deque(B)
    # 이분검색으로 큰 값 중 가장 작은 것을 찾고
    # 없다면 [0]부터 사용한다.
    
    for i in range(len(A)):
        bi = bisect.bisect_left(B, A[i])
        n = 0
        while n + bi < len(B):
            if A[i] < B[n+bi]:
                B.pop(bi+n)
                answer += 1
                break
            n += 1
            
    return answer

# 두번 째 풀이
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    for i in A:
        for j in B:
            if i < j:
                answer += 1
                B.remove(j)
                break            
    return answer

print(solution([5,1,3,7], [2,2,6,8]))
# print(solution([2,2,2,2],[1,1,1,1]))