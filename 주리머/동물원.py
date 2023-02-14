n = int(input())
zoo = [1, 3, 7] + [0] * (n - 2)

for i in range(2, n):
    zoo[i+1] = ((zoo[i] * 2) + zoo[i - 1]) % 9901

print(zoo[n])
