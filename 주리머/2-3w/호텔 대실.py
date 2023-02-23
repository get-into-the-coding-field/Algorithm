def cleaning(original):
    original = str(original).zfill(4)
    
    if original[2] == "5":
        original = int(original) + 50
    else:
        original = int(original) + 10
    return original

def solution(book_time):
    answer = []
    book_time = [[int("".join(time.split(":"))) for time in book] for book in book_time]
    book_time.sort(key=lambda x: x[0])
    
    for idx, b in enumerate(book_time):
        if idx == 0:
            # print("첫번째방이기 때문이 집어넣음")
            answer.append([b])
            continue
        
        isReserved = False
        for idx, reservation in enumerate(answer):
            reservationCloseTime = reservation[-1][1]
                
            if cleaning(reservationCloseTime) <= b[0]:
                # print("방 새로 내줄 준비 되어있음")
                isReserved = True
                answer[idx].append(b)
                break
                
        if not isReserved:
            answer.append([b])
            
    return len(answer)


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))
print(cleaning(855))



# 855 => 905
# 1450 => 1500
# 1458 => 1508