class person:
    def __init__(self):
        self.name = input("Enter name: ")
        self.address = input("Enter address: ")
        self.phn = int(input("Enter phone no. : "))
        self.email = input("Enter email: ")
        self.dob = input("Enter D.O.B. : ")

    def printinfo(self):
        print(f"name: {self.name}")
        print(f"address: {self.address}")
        print(f"phone no. : {self.phn}")
        print(f"email: {self.email}")
        print(f"D.O.B. : {self.dob}")


num = int(input("Enter number of people: "))

p = []

for i in range(num):
    print(f"\nFor person {i+1}:")
    p.append(person())


print()
for i in range(num):
    print(f"\n\nFor person {i + 1}:\n")
    p[i].printinfo()
