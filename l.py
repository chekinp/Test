def erer(d, q):
    fed = set(a)
    for c in d:
        if c in fed:
             q += 1
    if len(a) % 2 != 0:
        return False
    elif q == s:
        return True
    else:
        return False
q = 0
d = []
a = input()
s = len(a) // 2
for i in range(s):
    k = a[i]
    d.append(k)
print(erer(d, q))