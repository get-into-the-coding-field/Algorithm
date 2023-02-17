import sys

input = sys.stdin.readline
min_cost = sys.maxsize
n = int(input())
cities = []

for i in range(n):
    cities.append(list(map(int, input().split())))
    

def traveling(start, next, cost, visited):
    global min_cost
    
    if len(visited) == n:
        if cities[next][start] != 0:
            min_cost = min(min_cost, cost + cities[next][start])
        return
    
    for i in range(n):
        if cities[next][i] != 0 and i not in visited and cost < min_cost:
            visited.append(i)
            traveling(start, i, cost + cities[next][i], visited) 
            visited.pop()
    

for i in range(n):
    traveling(i, i, 0, [i])

print(min_cost)
'''
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
'''