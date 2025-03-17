n, l = map(int, input().split())
mas = list(map(int, input().split()))
mas.sort()
max_dist = 0
for i in range(len(mas) - 1):
    max_dist = max(max_dist, mas[i + 1] - mas[i])
print(max(max_dist / 2, max(mas[0] - 0, l - mas[-1])))