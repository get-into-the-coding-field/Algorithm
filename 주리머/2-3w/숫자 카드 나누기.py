def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solution(arrayA, arrayB):
    tmp = []
    for a in arrayA:
        if not tmp:
            tmp.append(a)
            continue
        else:
            tmp.append(gcd(a, tmp[-1]))
            
    tmp2 = []
    for b in arrayB:
        if not tmp2:
            tmp2.append(b)
            continue
        else:
            tmp2.append(gcd(b, tmp2[-1]))

    gcd1 = tmp[-1]
    gcd2 = tmp2[-1]

    for i in range(len(arrayA)):
        if gcd2 >= 1 and arrayA[i] % gcd2 == 0:
            gcd2 = 0
        
        if gcd1 >= 1 and arrayB[i] % gcd1 == 0:
            gcd1 = 0
        
    return max(gcd1, gcd2)



print(solution([10, 17], [5, 20]))
print(solution([10, 20], [5, 17]))
print(solution([14, 35, 119], [18, 30, 102]))
print(solution([50, 35, 90], [18, 27, 9]))
print(solution([12, 15, 18, 24, 36], [7, 14, 70, 35, 77]))
print(solution([20, 40, 10], [5, 17, 23]))