'''
디펜스 게임
(heapq로 풀이)
'''
import heapq as hq

def solution(n, k, enemy):
    answer = 0
    # 남은 병사 수보다 적들이 많을 때 사용
    enemyArr = []
    
    for idx, e in enumerate(enemy):
        
        n -= e
        hq.heappush(enemyArr, (-e, e))
        
        if n < 0:
            if k > 0:
                invincible = hq.heappop(enemyArr)[1]
                n += invincible
                k -= 1
            else:
                break
        answer += 1

    return answer

print(solution(7,3,[4, 2, 4, 5, 3, 3, 1]))
print(solution(2,4,[3, 3, 3, 3]))