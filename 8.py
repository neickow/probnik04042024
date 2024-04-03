from itertools import product
k=0
ans=0
for i in product('ЬРПЛЕА', repeat = 5):
    k += 1
    if i[-1] == 'Ь':
        ans += 1
    if k == 387:
        break
print(ans)