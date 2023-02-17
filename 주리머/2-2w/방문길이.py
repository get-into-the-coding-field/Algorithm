def solution(dirs):
    answer = 0
    # maps = [[0] * 11 for _ in range(11)]
    current = [5, 5]
    
    hash = {}
    for i in dirs:
        direction = ["L", "R", "U", "D"]
        move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        y, x = move[direction.index(i)]
        
        dy = current[0] + y
        dx = current[1] + x
        
        if 0 <= dy <= 10 and 0 <= dx <= 10:
            route = str(current[0]) + str(current[1]) + str(dy) + str(dx)
            reverseRoute = str(dy) + str(dx) + str(current[0]) + str(current[1])
            
            if route not in hash and reverseRoute not in hash:
                # print(f'route: {route}, reverseRoute: {reverseRoute}')
                hash[route] = 1
                hash[reverseRoute] = 1
                # print(f'hash: {hash}')
                answer += 1
            current = [dy, dx]
    return answer

# print(solution("ULURRDLLU")) # 7
# print(solution("LULLLLLLU")) # 7
print(solution("LRLRL")) # 1
# print(solution("LULLLLLLU")) # 7