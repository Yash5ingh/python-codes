m = int(input("uppar wala: "))
n = int(input("niche wala: "))
t = n - 1
s = m
res = m

while t > 0:
    m -= 1
    res *= m
    t -= 1
t = n

while t > 0:
    res //= t
    t -= 1

print(f"{s}C{n} = {res}")
