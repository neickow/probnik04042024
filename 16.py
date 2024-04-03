from functools import lru_cache
import sys
sys.setrecursionlimit(100000)
@lru_cache(None)
def f(n):
    if n >= 2025:
        return n
    else:
        return f(n+1)-f(n+2)+7

for i in range(2025, -1, -1):
    f(i)
print(f(15) - f(24))