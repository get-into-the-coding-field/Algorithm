'''
백준 11444. 피보나치수 6
https://www.acmicpc.net/problem/11444

# 참고
- https://www.acmicpc.net/blog/view/28
- https://ku-hug.tistory.com/122

'''
dictionary = {}
MOD = 1000000007
def fibo(n):
    if dictionary.get(n) != None:
        return dictionary[n]
    
    if n == 0:
        return 0
    
    if n == 1 or n == 2:
        return 1
    
    if n % 2 == 0:
        dictionary[n//2+1] = fibo(n//2+1) % MOD
        dictionary[n//2-1] = fibo(n//2-1) % MOD
        return dictionary[n//2+1] ** 2 - dictionary[n//2-1] ** 2
    else:
        dictionary[n//2+1] = fibo(n//2+1) % MOD
        dictionary[n//2] = fibo(n//2) % MOD
        return dictionary[n//2+1] ** 2 + dictionary[n//2] ** 2
    
print(fibo(int(input())) % MOD)