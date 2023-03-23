def solution(sticker):
    sticker_start = [0] + sticker[1:]
    sticker_end = [0] + sticker[:-1]
    length = len(sticker)
    
    if len(sticker) == 1:
        return sticker[0]
    
    for i in range(2, length):
        sticker_start[i] = max(sticker_start[i-1], sticker_start[i-2] + sticker_start[i])
    
    for i in range(2, length):
        sticker_end[i] = max(sticker_end[i-1], sticker_end[i-2] + sticker_end[i])
        
    return max(sticker_start + sticker_end)

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))