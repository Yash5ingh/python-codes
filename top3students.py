'''
dict = {}
ranks = []
rew = 5000

strength = int(input("enter number of students: "))

for i in range(strength):
    name = input(f"Enter name of student {i + 1}: ")
    mark = int(input(f"Enter marks of student {i + 1}: "))
    dict[mark] = name

for i in dict:
    ranks.append(i)

ranks.sort()
ranks.reverse()

print("\n\nNAME : MARKS")
for i in range(3):
    print(f"{i+1}. {dict[ranks[i]]} : {ranks[i]}   reward = Rs{rew}")
    rew -= 2000
'''

classData = []
rew = 5000
student = []
ranks = []

strength = int(input("enter number of students: "))

for i in range(strength):
    name = input(f"Enter name of student {i + 1}: ")
    mark = int(input(f"Enter marks of student {i + 1}: "))
    student.append(name)
    student.append(mark)
    classData.append(student)
    ranks.append(mark)
    student = []

ranks.sort()
ranks.reverse()

print("\n\nNAME : MARKS")
for i in range(3):
    for o in range(len(classData)):
        if ranks[i] == classData[o][1]:
            print(f"{i+1}. {classData[o][0]} : {ranks[i]}   reward = Rs{rew}")
            rew -= 2000
