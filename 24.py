fin = open('24.txt')
s = fin.readline()
fin.close()
l=0
i=0
mxl=0
while i < len(s):
    if s[i:i + 2] == 'EA':
        l += 2
        i += 2
    elif s[i:i + 3] == 'NPC':
        l += 3
        i += 3
    else:
        mxl = max(mxl, l)
        l = 0
        i += 1
print(mxl)