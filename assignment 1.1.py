def a():
    s = str1 + " " + str2
    return s


def b():
    i = 1
    while i <= 10:
        print(str2)
        i += 1


def c():
    print(f"length of str1= {len(str1)}")
    print(f"length of str2= {len(str2)}")


def d():
    print(final_str.upper())
    print(final_str.lower())
    print(final_str.capitalize())
    print(final_str.title())


def e():
    print(str1.replace("easy", "popular"))


def f():
    print(f"str1:\tstart='{str1[0]}'\tend='{str1[len(str1)-1]}'")
    print(f"str2:\tstart='{str2[0]}'\tend='{str2[len(str2) - 1]}'")


str1 = "Python programming is easy"
str2 = "Python programming is powerful and joyful"

print("\na.")
final_str = a()
print(final_str)
print("\nb.")
b()
print("\nc.")
c()
print("\nd.")
d()
print("\ne.")
e()
print("\nf.")
f()
