'''
백준 1918. 후위 표기식
https://www.acmicpc.net/problem/1918
'''

'''
+-는 후순위
*/ 선순위
'''
string_arr = list(input())
stack = []
result = ""

for string in string_arr:

    if string.isalpha():
        result += string
    else:
        if string == "(":
            stack.append(string)
        
        elif string in ("*", "/"):
            while stack and stack[-1] in ("*", "/"):
                result += stack.pop()
            stack.append(string)
        elif string in ("+", "-"):
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.append(string)
        elif string == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop()
    

while stack:
    result += stack.pop()
    
print(result)