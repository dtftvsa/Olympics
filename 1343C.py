t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    b = []
    curr = [l[0]]
    for i in range(0, len(l) - 1):
        if (l[i] > 0 and l[i + 1] > 0) or (l[i] < 0 and l[i + 1] < 0):
            curr.append(l[i + 1])
        else:
            b.append(curr)
            curr = [l[i + 1]]
    b.append(curr)
    sum = 0
    for i in b:
        sum += max(i)
    print(sum)