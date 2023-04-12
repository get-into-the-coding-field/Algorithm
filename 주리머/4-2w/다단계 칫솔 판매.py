'''
프로그래머스 Lv3. 다단계 칫솔 판매
https://school.programmers.co.kr/learn/courses/30/lessons/77486
'''

def solution(enroll, referral, seller, amount):
    
    def get_parent_idx(idx):
        if referral[idx] == '-':
            return '-'
        else:
            return pyramid[referral[idx]]
    
    def get_idx(name):
        return pyramid[name]
    
    def cal_share(price):
        return price - price // 10
        
    def cal_remain(price):
        return price // 10
        
    pyramid = {}
    top_arr = [i for i in range(len(enroll))]
    sales_arr = [0] * len(enroll)
    
    for idx, name in enumerate(enroll):
        pyramid[name] = idx
        
    for idx, name in enumerate(referral):
        if name != '-':
            top_arr[idx] = pyramid[name]

    for i in range(len(seller)):
        my_name = seller[i]
        my_idx = get_idx(my_name)
        parent_idx = get_parent_idx(get_idx(seller[i]))        
        # 부모가 없으면 100% 부모가 있으면 90%, 나머지를 10%로 변경
        
        if parent_idx == "-":
            sales_arr[my_idx] += cal_share(amount[i] * 100)
        else:
            # print(f'{my_name}의 판매 금액: {amount[i] * 100}원, 내가 받을 금액: {amount[i]*100*0.9} 부모에게 줄 금액: {remain}원')
            
            tot_amount = amount[i] * 100
            
            while parent_idx != my_idx and parent_idx != "-":
                sales_arr[my_idx] += cal_share(tot_amount)
                remain = cal_remain(tot_amount)
                
                # 피라미드 위로 하나 올라가기
                my_idx = parent_idx
                parent_idx = get_parent_idx(my_idx)

                # 자신이 피라미드 꼭대기라면 종료
                if parent_idx == "-":
                    sales_arr[my_idx] += cal_share(remain)
                    break
                
                # 부모에게 줄 금액 계산
                if cal_remain(tot_amount) > 0:
                    tot_amount = cal_remain(tot_amount)
                # 0원일 경우 종료
                else:
                    break
                    
    sales_arr = [int(i) for i in sales_arr]
    return sales_arr


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))
