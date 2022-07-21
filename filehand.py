filename = input("Enter name for the file: ")
ex = open(f"{filename}.txt", "w")
print(f"name: {ex.name}")
print(f"mode: {ex.mode}")

a = input("Enter contents for file: ")
while len(a) != 0:
    ex.write(a)
    ex.write("\n")
    a = input()

ex = open(f"{filename}.txt", "r")

b = ex.read()
print(b)

count = 0
searching = input("Enter character to search: ")
for i in b:
    if searching == i:
        count += 1

print(f"\n{searching} appeared {count} times.")

ex.close()
