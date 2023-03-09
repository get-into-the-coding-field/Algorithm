'''
프로그래머스 Lv1. 바탕화면 정리
https://school.programmers.co.kr/learn/courses/30/lessons/161990
'''

def solution(wallpaper):
    answer = [1e9, 1e9, 0, 0]
    
    
    n = len(wallpaper)
    m = len(wallpaper[0])
    
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == '#':
                if i < answer[0]:
                    answer[0] = i
                    
                if i > answer[2]:
                    answer[2] = i
                
                if j < answer[1]:
                    answer[1] = j
                    
                if j > answer[3]:
                    answer[3] = j
    answer[2] += 1
    answer[3] += 1
    return answer


print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))