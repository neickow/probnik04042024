fin = open('17.txt')
s = fin.readlines()
fin.close()
s = [int(i) for i in s]
m=0
k=0
ms=0
for i in s:
    if hex(i)[-2:] == '0f':
        m = max(m, i)
for i in range(len(s) - 1):
    if (s[i] % 7 == 0 and s[i + 1] % 7 != 0) or (s[i] % 7 != 0 and s[i + 1] % 7 == 0):
        if sum(s[i: i + 2]) % m == 0:
            k += 1
            ms = max(ms, sum(s[i: i + 2]))
print(k, ms)