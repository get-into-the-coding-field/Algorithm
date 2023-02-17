def solution(n, t, m, p):
    answer = '0'
    
    for i in range(1, t * m):
        answer += convertToN(i, n)

    return "".join([answer[idx] for idx in range(p-1, t * m, m)])

def convertToN(number, n):
    if number == 0:
        return '0'
    
    total = ""
    while number > 0:
        number, mod = divmod(number, n)
        
        if 10 <= mod <= 15 and n > 10:
            total += 'ABCDEF'[mod % 10]
        else:
            total += str(mod)
    
    return total[::-1]

print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))


# 진법 n, 
# 미리 구할 숫자의 갯수 t, 
# 게임에 참가하는 인원 m, 
# 튜브의 순서 p

# 1부터 증가시킨 수를 진수로 변환하여 반환한다.
# m명이 차례대로 부르고 튜브의 순서와 맞으면 answer에 추가한다.
# answer의 길이가 t와 같아지면 종료한다.

# 2	4	2	1	"0111"
# 16	16	2	1	"02468ACE11111111"
# 16	16	2	2	"13579BDF01234567"