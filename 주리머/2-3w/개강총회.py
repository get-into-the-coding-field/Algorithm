from collections import defaultdict

S, E, Q = [int("".join((i.split(":")))) for i in input().split()]

enter = defaultdict(int)
exit = defaultdict(int)
answer = 0
while True:
    try:
        time, name = input().split()
        time = int("".join(time.split(":")))
        
        if S >= time:
            if enter[name] == 0:
                enter[name] += 1
        
        if E <= time <= Q:
            if enter[name] == 1 and exit[name] == 0:
                exit[name] += 1
                answer += 1
                
    except:
        print(answer)
        break