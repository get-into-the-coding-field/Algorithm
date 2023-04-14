'''
프로그래머스 lv3. 자물쇠와 열쇠
https://school.programmers.co.kr/learn/courses/30/lessons/60059
'''

def solution(key, lock):
    start = len(key)-1
    end = start + len(lock)
    tot_size = start * 2 + len(lock)
    
    # 키를 90도로 회전시키는 함수
    def rotate_key(key):
        return [list(r) for r in zip(*key[::-1])] 
    
    # 보드에 키가 들어갈 수 있는지 확인하는 함수
    def isFit(rotated_key, dx, dy, board):
        # 보드에 키를 꼽아본다.
        for i in range(len(rotated_key)):
            for j in range(len(rotated_key)):
                board[i+dx][j+dy] += rotated_key[i][j]
        # 해당 키가 자물쇠를 열 수 있는 지 확인. 1이 아닌 게 있으면 False
        for i in range(start, end): 
            for j in range(start, end):
                # print(f'key의 위치: {i}, {j}, board의 값: {board[i][j]}')
                if board[i][j] != 1:
                    return False
        return True
    
    # 중간에 자물쇠를 끼워넣은 보드를 만드는 함수
    def generate_board():
        board = [[0] * (tot_size) for _ in range(tot_size)]
        for i in range(len(lock)):
            for j in range(len(lock)):    
                board[start+i][start+j] = lock[i][j]
        return board
    
    rotated_key = key
    
    for _ in range(4):
        rotated_key = rotate_key(rotated_key)
        for i in range(end):
            for j in range(end):
                board = generate_board()
                for x, y in [(i, j), (i, -j), (-i, j), (-i, -j)]:
                    if isFit(rotated_key, x, y, board):
                        return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))