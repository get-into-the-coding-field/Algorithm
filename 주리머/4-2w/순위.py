'''
프로그래머스 lv3. 순위
https://school.programmers.co.kr/learn/courses/30/lessons/49191
'''

from collections import defaultdict

def solution(n, results):
    winner_dict = defaultdict(set)
    loser_dict = defaultdict(set)
    answer = 0
    
    for winner, loser in results:
        winner_dict[winner].add(loser)
        loser_dict[loser].add(winner)
    
    for i in range(1, n+1):
        for loser in winner_dict[i]:
            print(f'loser: {loser}')
            loser_dict[loser].update(loser_dict[i])
            
        for winner in loser_dict[i]:
            print(f'winner: {winner}')
            winner_dict[winner].update(winner_dict[i])
    
    for i in range(1, n+1):
        if len(winner_dict[i]) + len(loser_dict[i]) == n-1:
            answer += 1
    return answer
print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))