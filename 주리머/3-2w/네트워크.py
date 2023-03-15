# dfs 사용    
def solution(n, computers):
    answer = 0
    visit = [0] * n
    
    def dfs(j):
        for idx, network in enumerate(computers[j]):
            if network == 1 and visit[idx] == 0:
                visit[idx] = 1
                dfs(idx)
        return
    
    for i in range(n):
        isFind = False
        
        for j in range(n):
            if i != j:
                # 연결되었다면
                if computers[i][j] == 1:
                    isFind = True
                    if visit[j] == 0:
                        # 연결횟수 추가
                        answer += 1
                        visit[i] = 1
                        visit[j] = 1
                        dfs(j)
        if not isFind:
            answer += 1
    return answer


# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1