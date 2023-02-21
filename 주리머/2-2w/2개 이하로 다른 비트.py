import math
def convertToBinary(n):
    return bin(n)[2:]
    
def solution(numbers):
    answer = []
    
    
    for n in numbers:
        binary = convertToBinary(n)
        
        count = 0
        for b in range(len(binary)-1, -1, -1):
            if binary[b] == '1':
                count += 1
            else:
                break
        
        val = math.ceil(n + (2**(count-1)))
        answer.append(val)
    return answer

print(solution([2, 7]))
print(solution([10,12,9,15,3,100000])); 
print(solution([1001,337,0,1,333,673,343,221,898,997,121,1015,665,779,891,421,222,256,512,128,100]))
# [1002, 338, 1, 2, 334, 674, 347, 222, 899, 998, 122, 1019, 666, 781, 893, 422, 223, 257, 513, 129, 101]