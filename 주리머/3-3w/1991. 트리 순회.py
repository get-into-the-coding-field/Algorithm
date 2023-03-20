'''
백준 1991. 트리 순회
https://www.acmicpc.net/problem/1991
'''

n = int(input())
dict = {}
forward = ""
middle = ""
backward = ""

def 전위순회(node):
    global forward
    forward += node
    
    if dict[node][0] != '.':
        전위순회(dict[node][0])
    
    if dict[node][1] != '.':
        전위순회(dict[node][1])
    
def 중위순회(node):
    global middle
    
    if dict[node][0] != '.':
        중위순회(dict[node][0])
        
    middle += node
    
    if dict[node][1] != '.':
        중위순회(dict[node][1])
    

def 후위순회(node):
    global backward
    
    if dict[node][0] != '.':
        후위순회(dict[node][0])
    
    if dict[node][1] != '.':
        후위순회(dict[node][1])
    
    backward += node
    
for _ in range(n):
    node, left, right = input().split()
    dict[node] = [left, right]

전위순회('A')
중위순회('A')
후위순회('A')

print(forward)
print(middle)
print(backward)