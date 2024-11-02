n = input()
end = ""
l = ["a", "o", "y", "e", "u", "i"]
n = n.lower()
for i in l:
    n = n.replace(i, "")
n = list(n)
for i in n:
    end += "." + i
print(end)