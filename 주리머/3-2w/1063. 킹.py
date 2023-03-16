'''


A1 A2 5
B
L
LB
RB
LT

'''
king, rock, m = input().split()
king = [k if i == 0 else int(k) for i, k in enumerate(king)]
rock = [k if i == 0 else int(k) for i, k in enumerate(rock)]
direction = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
coordinate = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
row = 'ABCDEFGH'

for _ in range(int(m)):
    # 킹을 움직였을 때 안 벗어나는 지 체크
    # 돌과 같은 위치인 지 확인
    # 돌이 밀렸을 때 안 벗어나는 지 체크
    # 벗어나면 무시
    # 안벗어나면 돌과 킹을 옮긴다.    
    def checkGetOut(cur):
        return cur[0] in row and 0 < int(cur[1]) <= 8
    
    def move(cur, dir):
        nx = chr(ord(cur[0]) + dir[1])
        ny = cur[1] + dir[0]
        return [nx, ny]
    
    d = input()
    idx = direction.index(d)
    dir = coordinate[idx]
    
    if checkGetOut(move(king, dir)):
        
        if move(king, dir) == rock:
            if checkGetOut(move(rock, dir)):
                king = move(king, dir)
                # print(f'dir: {dir}, king 결과: {king}')
                rock = move(rock, dir)
                # print(f'dir: {dir}, rock 결과: {rock}')
        else:
            # print(f'dir: {dir}, king만 움직인 결과: {king}')
            king = move(king, dir)
    
king[1] = str(king[1])
rock[1] = str(rock[1])
print("".join(king))
print("".join(rock))
        