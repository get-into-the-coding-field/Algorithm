# 가로, 세로로 붙어있거나, 빈테이블 사이로 대각선에 사람이 존재하면 X
# 한명이라도 지키지 않으면 0을 담음
# P(자리), 0(테이블), X(파티션)

def solution(places):
    answer = []
    direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    

    def inspection(x, y, waiting_room):
        
        
        for m in range(4):
            dx = x + direction[m][0]
            dy = y + direction[m][1]
            
            if 0 <= dx < 5 and 0 <= dy < 5:
                if waiting_room[dx][dy] == 'P':
                    return False
                
                if waiting_room[dx][dy] == "O":
                    # 빈테이블 사이에 자리 있나 확인
                    ddx = dx + direction[m][0]
                    ddy = dy + direction[m][1]
                    if 0 <= ddx < 5 and 0 <= ddy < 5:
                        if waiting_room[dx + direction[m][0]][dy + direction[m][1]] == "P":
                            return False
                    # 세로에 벽이 있기 때문에 가로에 자리 있나 확인
                    if m <= 1:
                        if dy > 0:
                            if waiting_room[dx][dy-1] == "P":
                                return False
                        
                        if dy < 4:
                            if waiting_room[dx][dy+1] == "P":
                                return False
                    # 가로에 벽이 있기 때문에 세로에 자리 있나 확인
                    else:
                        if dx > 0:
                            if waiting_room[dx-1][dy] == "P":
                                return False
                        
                        if dx < 4:
                            if waiting_room[dx+1][dy] == "P":
                                return False
        return True

    for p in places:
        waiting_room = [list(i) for i in p]
        
        isFindBadBoy = False
        for i in range(5):
            for j in range(5):
                if waiting_room[i][j] == "P":
                    if not inspection(i, j, waiting_room):
                        answer.append(0)
                        isFindBadBoy = True
                        break
            if isFindBadBoy:
                break
        if not isFindBadBoy:
            answer.append(1)

    return answer

print(solution([["XOOOP", 
                 "OPXOX", 
                 "OOOXX", 
                 "OPXOX", 
                 "XOXXP"], 
                
                ["POOPX", 
                 "OXPXP", 
                 "PXXXO", 
                 "OXXXO", 
                 "OOOPP"], 
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))