'''
백준 13305. 주유소
https://www.acmicpc.net/problem/13305

4
2 3 1
5 2 4 1

'''

# 해당 주유소까지의 가장 싼 값으로 거래하기
n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
minPrices = 1e9
total = 0

for i in range(n-1):
    if prices[i] < minPrices:
        minPrices = prices[i]
    
    total += minPrices * distances[i]
    
print(total)
