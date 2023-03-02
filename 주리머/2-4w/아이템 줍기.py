'''
프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/87694
'''
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    # 점선대로 도형을 그리되, 안은 채우지 않는다. => 채워야한다.. 못가게 막기 위해서
    maps = [[0] * (102) for _ in range(102)]
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for idx, r in enumerate(rectangle):
        x1, x2 = r[0] * 2, r[2] * 2
        y1, y2 = r[1] * 2, r[3] * 2
        # 도형 겉만 그리고, 속은 못가게 9처리

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if (i == x1 or i == x2) or (j == y1 or j == y2):
                    if maps[i][j] == 0:
                        maps[i][j] = idx + 1
                else:
                    maps[i][j] = 9
    
    for m in maps:
        print(m)
    q = deque()
    q.append((characterX, characterY , 0, [[characterX, characterY]]))
    
    while q:
        x, y, count, visit = q.popleft()
        
        # print(x, y, count, visit)
        
        
        for i in range(4):
            dx = direction[i][0] + x
            dy = direction[i][1] + y
            
            if 0 <= dy <= 102 and 0 <= dx <= 102 and 1 <= maps[dx][dy] <= 4 and [dx, dy] not in visit:
                if dy == itemY and dx == itemX:
                    # print(f'정답: {visit} + {dx, dy}')
                    return (count + 1) // 2
                q.append((dx, dy, count + 1, visit + [[dx, dy]]))
        
    return 0

# print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)) # 17
print(solution([[1,1,5,7]],1,1,4,7)) # 9
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3)) # 10

print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1)) # 11
# 1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4]] + (3, 6)

'''

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 7, 1, 0, 0, 0, 0, 0]
[0, 1, 9, 9, 1, 0, 4, 4, 4, 0]
[0, 1, 9, 9, 1, 2, 4, 9, 4, 0]
[0, 1, 9, 9, 9, 2, 3, 9, 3, 3]
[0, 1, 9, 9, 9, 9, 9, 9, 9, 3]
[0, 1, 9, 9, 1, 3, 3, 9, 7, 3]
[0, 1, 1, 1, 1, 0, 4, 9, 3, 0]
[0, 0, 0, 0, 0, 0, 4, 4, 4, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

[[1, 3], [1, 4], [2, 4], [3, 4], [3, 5], [3, 6], [2, 6], [2, 7], [2, 8], [3, 8], [4, 8], [4, 9], [5, 9], [6, 9], [6, 8]] + (7, 8)

[1, 3] => 7, 8
'''