str1 = "Python programming is easy "
str2 = "Python programming is powerful and joyful"
print("string 1: ", str1)
print("string 2: ", str2)
# adding two strings
str = str1 + str2
print("addition of two strings : ", str)

# printing str2 10 times
print(10 * (str2 + '\n'))

# finding length of strings
print(len(str1))
print(len(str2))

# Converting String str to Upper, Lower, Title, Capitalization
str = str1 + str2
print("addition of two strings : ", str)
print(str.upper())
print(str.lower())
print(str.title())
print(str.capitalize())

# replace easy from str1 to popular and print again
str = str1.replace('easy', 'popular')
print("Replaced string : ", str)

# Find Start and End of both the String and show to users
print(str1.startswith("Python"))
print(str1.endswith("easy"))
print(str2.startswith("Python"))
print(str2.endswith("joyful"))
