n = int(input())
s = int(input())
word = input().strip()

find = "I" + ("OI" * n)
answer = 0

for i in range(s-(2 * n)):
    if word[i] == "I":
        if word[i:i + len(find)] ==  find:
            answer += 1
print(answer)