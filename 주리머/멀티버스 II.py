from collections import defaultdict
n, m = map(int, input().split())
universe = defaultdict(int)

for i in range(n):
    planet = list(map(int, input().split()))
    sorted_planet = sorted(list(set(planet)))
    # index_arr = tuple([sorted_planet.index(i) for i in planet])
    
    dict_arr = {sorted_planet[i]: i for i in range(len(sorted_planet))}
    c = tuple([dict_arr[i] for i in planet])
    print(sorted_planet, dict_arr, c)
    universe[c] += 1
    # print(universe)
sum = 0

for i in universe.values():
    sum += (i * (i - 1)) // 2

print(sum)
    


    


'''
2 3
1 3 2
12 50 31
'''
