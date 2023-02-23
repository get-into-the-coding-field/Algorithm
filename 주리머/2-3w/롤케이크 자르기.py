'''
롤 케이크 자르기
https://school.programmers.co.kr/learn/courses/30/lessons/132265
(해시 잘 사용하기)
'''
from collections import Counter

def solution(topping):
    answer = 0
    youngerBrother = set()
    bigBrother = Counter(topping)
    
    
    while topping:
        t = topping.pop()
        bigBrother[t] -= 1
        
        if bigBrother[t] == 0:
            del bigBrother[t]
            
        youngerBrother.add(t)
        
        if len(bigBrother) == len(youngerBrother):
            answer += 1
    
    return answer



# 2가지 배열을 만들어서 하나는 뒤쪽에서부터의 조합
# 다른 하나는 앞쪽에서부터의 조합
# 이후 두 배열을 비교하여 1차이 나는 곳을 +1한다.

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))