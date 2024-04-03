mx=-10**20
# 27Ax23 16 + 8yE5D2 16
for x in range(16):
    for y in range(16):
        s1=int('27a023', 16) + x * 16 ** 2
        s2=int('80e5d2', 16) + y * 16 ** 4
        if (s1+s2)%5==0:
            mx=max(mx, x+y)
print(mx)