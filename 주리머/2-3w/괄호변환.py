def divide(p):
    left = 0
    right = 0
    
    for i in p:
        if i == "(":
            left += 1
        else:
            right += 1
        
        if left == right:
            return p[:left+right], p[left+right:]

def check(u):
    return u.count(")") == u.count("(")

def solution(p):
    
    # 1단계
    if not p:
        return ""
    
    # 2단계
    u, v = divide(p)
    
    # 3단계
    if check(u):
        # 3-1단계
        u += solution(v)
        return u
    # 4단계
    else:
        # 4-1단계
        answer = "("
        # 4-2 단계
        answer += solution(v)
        # 4-3 단계
        answer += ")"
        
        # 4-4단계
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)
        
        return answer

print(solution(""))
print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))

