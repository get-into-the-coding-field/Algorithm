def solution(park, routes):
    n = len(park)
    m = len(park[0])
    park = [list(p) for p in park]
    cur = [0, 0]
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                cur = [i, j]
    
    def isHurdle(pos):
        
        # 이 부분 다시 수정
        return park[pos[0]][pos[1]] == 'X'
    
    def canMove(pos, op, num):
        if op == "E":
            changed = pos[1]
            for i in range(num):
                changed += 1
                if not (0 <= changed < m) or isHurdle([pos[0],changed]):
                    return False
            else:
                return True
            
        if op == "W":
            changed = pos[1]
            for i in range(num):
                changed -= 1
                if not (0 <= changed < m) or isHurdle([pos[0],changed]):
                    return False
            else:
                return True
        
        if op == "S":
            changed = pos[0]
            for i in range(num):
                changed += 1
                if not (0 <= changed < n) or isHurdle([changed,pos[1]]):
                    return False
            else:
                return True
        
        if op == "N":
            changed = pos[0]
            for i in range(num):
                changed -= 1
                if not (0 <= changed < n) or isHurdle([changed, pos[1]]):
                    return False
            else:
                return True
    
    def move(pos, op, num):
        if op == "E":
            return [pos[0], pos[1]+num]
        
        if op == "W":
            return [pos[0], pos[1]-num]
        
        if op == "S":
            return [pos[0]+num, pos[1]]
        
        if op == "N":
            return [pos[0]-num, pos[1]]
        return 
        
    for route in routes:
        op, num = route.split()
        num = int(num)
        
        if canMove(cur, op, num):
            cur = move(cur, op, num)
    
    return cur

print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]	))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))