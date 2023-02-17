waves = [0] * 101
waves[0:9] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]


for i in range(int(input())):
    n = int(input())
    
    
    for i in range(10, n + 1):
        waves[i] = waves[i-1] + waves[i-5]
    
    print(waves[n-1])