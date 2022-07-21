s1 = {1, 2, 3}
s2 = {2, 3, 4}
print("union:", s1 | s2)
# b. Set difference
s1 = {1, 2, 3, 4, 8}
s2 = {1, 3, 8, 4, 6}
Result = s1.difference(s2)
print("Result:", Result)
Result = s2.difference(s1)
print("Result:", Result)
print("Intersection:", s1 & s2)
# c. Set intersection
s1 = {2, 4, 6, 8, 10, 11}
s2 = {1, 3, 5, 7, 9, 11}
s3 = {2, 3, 8, 9, 11}
Result = s1.intersection(s2, s3)
print("Result:", Result)
# d. Set Complement
U = {1, 2, 3, 4, 5, 6, 7}
a = {1, 2, 3}
b = {3, 4, 5}
Comp_a = U - a
Comp_b = U - b
Result = Comp_a.intersection(Comp_b)
print("Result:", Result)
