'''
백준 1340. 연도진행바
https://www.acmicpc.net/problem/1340
'''
calendar = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, D, Y, T = input().split()
tot_day = 365

# 윤년 처리
if int(Y) % 400 == 0 or (int(Y) % 4 == 0 and int(Y) % 100 != 0):
    day[1] = 29
    tot_day += 1
    
tot_time = tot_day * 24 * 60
D = D.split(",")[0]
H, M = map(int, T.split(':'))
current_time = sum([day[i] for i in range(calendar.index(month))]) * 24 * 60 + ((int(D)-1) * 24 * 60) + H * 60 + M

print(current_time / tot_time * 100)



# 윤년은 그 해가 400으로 나누어 떨어지는 해 이거나, 4로 나누어 떨어지면서, 100으로 나누어 떨어지지 않는 해 일때이다. 지역에 따른 서머타임