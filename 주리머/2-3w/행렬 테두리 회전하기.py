def solution(rows, columns, queries):
    answer = []
    matrix = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = i * columns + j + 1
    
    for query in queries:
        r1, c1, r2, c2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        stack = []
        
        for i in range(c1, c2 + 1):
            stack.append(matrix[r1][k])
            
            if len(stack) == 1:
                continue
            else:
                matrix[r1][k] = stack[-2]

        for j in range(r1 + 1, r2 + 1):
            stack.append(matrix[c2][k])
            matrix[c2][k] = stack[-2]
            
        for k in range(c2 - 1, c1 - 1, -1):
            stack.append(matrix[r2][k])
            matrix[r2][k] = stack[-2]
        
        for k in range(r2 - 1, r1 - 1, -1):
            stack.append(matrix[k][c1])
            matrix[k][c1] = stack[-2]
        
        answer.append(min(stack))
    
    for i in matrix:
        print(i)
    return answer

print(solution(6,6,[[2,2,5,4]]))
# print(solution(6,6,[[2,2,5,4]]))