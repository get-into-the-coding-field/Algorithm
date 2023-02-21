import heapq as hq
def solution(users, emoticons):
    answer = []
    
    for sale in range(40, 0, -1):
        membershipCount = 0
        sales = 0 
        total = sum(emoticons) * (100 - sale) // 100
        
        for [wantSales, limitCost] in users:
            if total >= limitCost:
                membershipCount += 1
            else:
                if wantSales <= sale:
                    sales = total
        
        hq.heappush(answer, [-membershipCount, sales])
        
        print(f'{sale}%, {total}')
    
    return hq.heappop(answer)


print(solution([[40, 10000], [25, 10000]], [7000, 9000])) # [1, 5400]
# print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])) # [4, 13860]
