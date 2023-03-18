'''
백준 13699. 점화식

t(0)=1
t(n)=t(0)*t(n-1)+t(1)*t(n-2)+...+t(n-1)*t(0)
이 정의에 따르면,

t(1)=t(0)*t(0)=1
t(2)=t(0)*t(1)+t(1)*t(0)=2
t(3)=t(0)*t(2)+t(1)*t(1)+t(2)*t(0)=5
'''

n = int(input())
memo = [1, 1, 2, 5]
answer = 0

for i in range(4, n+1):
    tot = 0
    
    for j in range(i):
        tot += memo[j] * memo[i-j-1]
    
    memo.append(tot)

print(memo[n])