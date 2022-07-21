# palindrme
num = 101
rev = 0
while num > 0:
    r = int(num % 10)
    rev = int((rev * 10) + r)
    num = int(num / 10)
print(rev)
