target = input()
n = int(input())
answer = 0

for _ in range(n):
    word = input()
    word = word * 2
    if word.find(target) > -1:
        answer += 1
        
print(answer)