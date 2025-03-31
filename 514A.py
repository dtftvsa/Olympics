a = int(input())
b = ""
while a != 0:
    c = a % 10
    if c > 4:
        if len(str(a)) > 1:
            b = str(9 - c) + b
        else:
            if c == 9:
                b = str(c) + b
            else:
                b = str(9 - c) + b
    else:
        b = str(c) + b
    a //= 10
print(b)