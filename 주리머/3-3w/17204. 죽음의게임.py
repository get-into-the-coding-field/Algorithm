'''
백준 17204. 죽음의게임
https://www.acmicpc.net/problem/17204
'''


    


        
def solution():
    def dfs(start, num):
        print(f'dfs 도착!!! start: {start}, num: {num}')
        # 무한 츠쿠요미
        if num == m:
            return True
        
        if num == start:
            return False
    
            
        return dfs(start, arr[num])
    n, m = map(int, input().split())
    arr = [0] * (n+1)


    for i in range(n):
        arr[i+1] = int(input())
    
    print(f'arr: {arr}')
    for idx in range(n):
        if dfs(idx, arr[idx]):
            return idx
    return -1
    
print(solution())