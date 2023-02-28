'''
18111. 마인크래프트
https://www.acmicpc.net/problem/18111


3 4 99
0 0 0 0
0 0 0 0
0 0 0 1

'''

# 땅의 높이가 같은 것이 많은 쪽을 기준으로 높이를 맞춰준다. (hash를 사용하면 O(n))
# min_height와 max_height 사이를 모두 순회하면서 작은 time을 찾아준다.


from collections import Counter
n, m, block = map(int, input().split())

mine = sum([list(map(int, input().split())) for _ in range(n)],[])
minHeight = 257
maxHeight = -1
time = 1000000000
answerHeight = 0
hash = Counter(mine)
maxHeight = max(mine)
minHeight = min(mine)    


for height in range(minHeight, maxHeight+1):
        isPossible = True
        tmpTime = 0
        tmpBlock = block
        
        for [key, val] in sorted(hash.items(), key=lambda x: x[0], reverse=True):
            if key > height:
                tmpTime += (key - height) * val * 2
                tmpBlock += (key - height) * val
                    
            else:
                if tmpBlock >= (height - key) * val:
                    tmpTime += (height - key) * val
                    tmpBlock -= (height - key) * val
                else:
                    isPossible = False
                    break
            if not isPossible:
                break
        
        if isPossible and time >= tmpTime:
            time = tmpTime
            answerHeight = height
            
print(time, answerHeight)

'''
2 2 35
20 10
190 40

350 40

2 2 68
120 90
250 170

290 170
'''
