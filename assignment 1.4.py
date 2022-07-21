def usingfor(a):
    for i in range(1, a + 1):
        if i < 10:
            print(i, end=", ")
        else:
            print(i, end=",")
        if i % 10 == 0:
            print("\b")
    print("\b")


def usingwhile(a):
    i = 1
    while i <= a:
        if i < 10:
            print(i, end=", ")
        else:
            print(i, end=",")
        if i % 10 == 0:
            print("\b")
        i += 1
    print("\b")


num = int(input("enter a number: "))
print("\nUsing for loop:")
usingfor(num)
print("\nUsing while loop:")
usingwhile(num)
