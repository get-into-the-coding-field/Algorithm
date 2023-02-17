n = int(input())
s = int(input())
word = input().strip()

idx = 0
count = 0
answer = 0
while idx < s - 1:
    
    if word[idx:idx+3] == "IOI":
        idx += 2
        count += 1
    
        if n <= count:
            answer += 1
    else:
        idx += 1
        count = 0

print(answer)

        