'''
마법의 엘리베이터
https://school.programmers.co.kr/learn/courses/30/lessons/148653
'''

from collections import deque
def solution(storey):
    q = deque()
    q.append((storey, 0))
    
    while q:
        n, count = q.popleft()
        n = str(n)
        length = len(n)
        
        if n == '0':
            return count
        
        # 반올림해서 해당 숫자에서 제외 시킨다.
        for i in range(len(n)-1, -1, -1):
            
            if n[i] == '0':
                continue
            
            # round 사사오입 원칙으로 임의로 5를 4로 바꿔서 반올림
            if n[i] == '5':
                if i > 0 and int(n[i-1]) > 4:
                    n = n[:i] + '6' + n[i+1:]
                    count += 1
                elif i > 0 and int(n[i-1]) < 5:
                    n = n[:i] + '4' + n[i+1:]
                    count += 1  
                
            rounded = round(int(n), -((length - i)))
            diff = abs(rounded - int(n)) // (10 ** (length - i - 1))
            
            if i == 0:
                # ex) 600 -> 1000 반올림 됐을 때 자릿수가 더 해지는 경우 count를 더해준다.
                if len(str(rounded)) > len(n):
                    count += len(str(rounded)) - len(n)
                return count + max(diff, 1)
            
            q.append((rounded, count + diff))
            break

print(solution(16))
print(solution(2554))
# print(solution(545))
# print(solution(155))
# print(solution(154))
# print(solution(75))
print(solution(555))