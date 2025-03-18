def func(n, m, a, b):
    l = []
    ans = 0
    count = 0
    l.append(n * a)
    while n - count > m:
        count += m
        ans += b
    if (ans + ((n - count) * a) < ans + b):
        l.append(ans + ((n - count) * a))
    else:
        l.append(ans + b)
    return min(l)

n, m, a, b = map(int, input().split())
ans = 0
count = 0
print(func(n, m, a, b))