'''
https://www.acmicpc.net/problem/1764

3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
'''

n, m = map(int, input().split())
answer = []
obj = {}
for i in range(n):
    obj[input()] = 1
    
for j in range(m):
    name = input()
    if name in obj:
        answer.append(name)
        

print(len(answer))
for a in sorted(answer):
    print(a)