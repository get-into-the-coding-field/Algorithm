'''
백준 17626. Four squares
https://www.acmicpc.net/problem/17626
'''
# 다시 풀기
import math

def findFourSquares(n):

    if int(math.sqrt(n)) == math.sqrt(n):
        return 1
    
    for i in range(1, int(math.sqrt(n))+1):
        if int(math.sqrt(n-i*i)) == math.sqrt(n-i*i):
            return 2
    
    for i in range(1, int(math.sqrt(n))+1):
        for j in range(1, int(math.sqrt(n-i**2))+1):
            if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
                return 3    
    return 4
print(findFourSquares(int(input())))
