import math

def convertToN(n, k):
    sum = ""
    
    while n > 0:
        n, mod = divmod(n, k)
        sum += str(mod)
    return sum[::-1]
        
def checkPrimeNumber(n):
    n = int(n)
    
    if n == 1:
        return False
    
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    converted = ""
    
    if k != 10: 
        converted = convertToN(n, k)    
    else:
        converted = str(n)
        
    chr = ""
    # 마지막 계산을 위한 보정
    converted = converted + "0"
    
    for i in range(len(converted)):
        if converted[i] != "0":
            chr += converted[i]
        else:
            if chr != "":
                if checkPrimeNumber(chr):
                    answer += 1
                chr = ""
    return answer

# 211020101011
# 211 2 11  1, 1
print(solution(437674, 3))
print(solution(110011, 10))
print(solution(18, 9))

'''
0P0처럼 소수 양쪽에 0이 있는 경우 --- O
P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
P처럼 소수 양쪽에 아무것도 없는 경우
단, P는 각 자릿수에 0을 포함하지 않는 소수입니다
'''