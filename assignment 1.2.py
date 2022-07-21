def is_equilateral(a, b, c):
    if a == b == c:
        print("Equilateral")


def is_isosceles(a, b, c):
    if a == b != c or b == c != a or c == a != b:
        print("Isosceles")


def is_scalene(a, b, c):
    if a != b != c:
        print("Scalene")


print("Enter sides of a triangle: ")
s1 = int(input())
s2 = int(input())
s3 = int(input())

is_equilateral(s1, s2, s3)
is_isosceles(s1, s2, s3)
is_scalene(s1, s2, s3)
