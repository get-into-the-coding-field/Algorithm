'''

5457
3
6 7 8

'''

target = int(input())
n = int(input())
banned = []
count = 0
current_channel = ""

if n != 0:
    banned = list(input().split())

min_count = abs(target - 100)

for i in range(1000001):
    str_num = str(i)
    
    for s in str_num:
        if s in banned:
            break
        
    else:
        min_count = min(min_count, abs(int(str_num) - target) + len(str_num))

print(min_count)