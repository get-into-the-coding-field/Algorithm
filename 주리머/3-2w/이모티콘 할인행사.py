def solution(users, emoticons):
    discount_rate = [10, 20, 30, 40]
    discount_list = [0] * len(emoticons)
    n, m = len(users), len(emoticons)
    global answer
    answer = [-1, -1]
    
    def dfs(idx):
        global answer
        if idx == m:
            # print(f'idx: {idx}, discount_list: {discount_list}')
            subscribe = 0
            sales = 0

            for user in users:
                # 유저마다 할인율 이상인 경우 구매
                price = 0
                for i in range(m):
                    if user[0] <= discount_list[i]:
                        price += int((100 - discount_list[i]) * emoticons[i] / 100)

                if price >= user[1]:
                    subscribe += 1
                else:
                    sales += price
                # print(f'price: {price}')


            # print(f'subscribe: {subscribe}, sales: {sales}, answer: {answer}')
            if subscribe > answer[0] or (subscribe == answer[0] and sales > answer[1]) :
                answer = [subscribe, sales]
            return
        
        for i in range(4):
            discount_list[idx] = discount_rate[i]
            dfs(idx + 1)
    
    dfs(0)
    return answer

print(solution([[40, 10000], [25, 10000]],[7000, 9000])) # 	[1, 5400]