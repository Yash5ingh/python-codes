# 3. Write a program to perform the following on List
# a. Enter a List of Numbers and sort the value in Largest-to-smallest order.
lis1 = [20, 30, 45, 78, 94]
my_list = sorted(lis1, reverse=True)
print(my_list)
# Do the same thing, but for strings and in reverse alphabetical order.
str1 = ["hi", "byee", "hello", "mango", "song"]
order1 = str1.sort(reverse=True)
print(str1)
# Create a list with elements as "apple", “banana",”cherry", "kiwi", “melon", "mango". Display each with its position
lis2 = ["apple", "cherry", "kiwi", "melon", "mango"]
for i in range(len(lis2)):
    print(f"{i}: {lis2[i]}")
# inserting orange
lis3 = lis2.append("Orange")
print(lis3)
# removing cherry
lis5 = lis2.remove("cherry")
print("Removing Cherry", lis5)
# 3rd 4th and 5th element
print("3rd 4th and 5th elements are:", lis2[2:5])
# checking if apple is present
for i in lis2:
    if (i == "Apple"):
        print("Apple is present in list")
# prenting element one by one
print("Seperated list:")
print(*lis2, sep="\n")
# removing index 3 and pop
lis2 = ["apple", "Banana", "cherry", "kiwi", "melon", "mango"]
lis5 = lis2.pop(3)
print("popping index 3:")
print(lis5)
print(lis2)
