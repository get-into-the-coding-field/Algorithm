'''

'''

def solution(n, l, r):
    q_l = quin(l - 1)
    q_r = quin(r)
    count_l = decode(q_l)
    count_r = decode(q_r)
    return count_r - count_l

def quin(n) :
    result = []
    while n > 0 :
        n,mod = divmod(n,5)
        result.append(mod)
    return result[::-1]

def decode(quinary) :
    result = 0
    length = len(quinary)
    dec = [0, 1, 2, 2, 3]
    for i, x in enumerate(quinary) :
        exponent = length-i-1
        result += (4**exponent)*dec[x]
        if x == 2 :
            break    
    return result



print(solution(3, 5, 9))
# print(solution(4,30,118))# 39
# print(solution(3,1,125))# 64

# 110[11110110000011]01111011