# zero and 1
list = [1]
zeroes = 0
run = True
while run:
    for i in range(zeroes):
        list.append(0)
    list.append(1)
    if zeroes == 10:
        run = False
    zeroes += 1
print(list)


len = int(input("Enter length in cm: "))
if len < 0:
    print("Invalid input")
else:
    inch = len / 2.54
    print(len, "centimetres is equal to ", inch, " inches")