
print('19 ЗАДАНИЕ')
def f(s, p=1):
    if p==3 and s>=82:
        return True
    if (p!=3 and s>=82) or (p==3 and s<82):
        return False

    #p
    if p%2==1:
        return f(s+10, p+1) or f(s*2, p+1)
    else:
        return f(s + 10, p + 1) and f(s * 2, p + 1)

for s in range(1, 82):
    if f(s):
        print(s)
        break
print('20 ЗАДАНИЕ')

def f(s, p=1):
    if p in (2, 4) and s >= 82:
        return True
    if (p == 3 and s >= 82) or (p == 4 and s < 82):
        return False

    # p
    if p % 2 == 1:
        return f(s + 10, p + 1) and f(s * 2, p + 1)
    else:
        return f(s + 10, p + 1) and f(s * 2, p + 1)

locked = []
for s in range(1, 82):
    if f(s):
        locked.append(s)
def f(s, p=1):
    if p in (2, 4) and s >= 82:
        return True
    if (p == 3 and s >= 82) or (p == 4 and s < 82):
        return False

    # p
    if p % 2 == 1:
        return f(s + 10, p + 1) and f(s * 2, p + 1)
    else:
        return f(s + 10, p + 1) or f(s * 2, p + 1)


for s in range(1, 82):
    if f(s) and s not in locked:
        print(s)
print('21 ЗАДАНИЕ')
def f(s, p=1):
    if p in (3, 5) and s >= 82:
        return True
    if (p not in (3, 5) and s >= 82) or (p == 5 and s < 82):
        return False

    # p
    if p % 2 == 1:
        return f(s + 10, p + 1) or f(s * 2, p + 1)
    else:
        return f(s + 10, p + 1) and f(s * 2, p + 1)


for s in range(1, 82):
    if f(s):
        print(s)
        break