f=open('27A.txt')
s=f.readlines()
f.close()
N=int(s.pop(0))
s=[int(x) for x in s]
mns=10**20
for i in range(N-1):
    for j in range(i+1, len(s)):
        if s[i]<s[j] and (s[i]+s[j])%144==0:
            mns=min(mns, s[i]+s[j])
print(mns)