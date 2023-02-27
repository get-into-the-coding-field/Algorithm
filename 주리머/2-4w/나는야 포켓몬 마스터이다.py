'''
백준 class 2문제
https://www.acmicpc.net/problem/1620

26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna
'''

n, m = map(int, input().split())
pokemon = []
answer = []

for i in range(n):
    name = input()
    pokemon.append(name)

for i in range(m):
    a = input()
    if not a.isdigit():
        answer.append(pokemon.index(a)+1)
    else:
        answer.append(pokemon[int(a)-1])
    
for a in answer:
    print(a)
        
    

