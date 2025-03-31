n = int(input())
sum, best = 0, 0
l = list(map(int, input().split()))
init = l.count(1)
l1 = [1 if x == 0 else -1 for x in l]
for i in range(len(l1)):
    sum = max(l1[i], sum + l1[i])
    best = max(best, sum)
if init == n:
    print(init - 1)
else:
    print(best + init)