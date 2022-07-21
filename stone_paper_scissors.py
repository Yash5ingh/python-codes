import random

ps = 0
cs = 0

name = input("enter your name: ")
end = int(input("first to reach: "))

while ps != end and cs != end:
    p = int(input("\nstone : 1\npaper : 2\nscissors : 3\n\nenter your choice: "))
    c = random.randint(1, 3)
    print("\n\n")

    if c == 1:
        print("stone!\n")

        if p == 1:
            print("draw")
        elif p == 2:
            print("you win!!")
            ps += 1
        else:
            print("you lose!")
            cs += 1

    elif c == 2:
        print("paper!\n")

        if p == 1:
            print("you lose!")
            cs += 1
        elif p == 2:
            print("draw")
        else:
            print("you win!!")
            ps += 1

    else:
        print("scissors!\n")

        if p == 1:
            print("you win!!")
            ps += 1
        elif p == 2:
            print("you lose!")
            cs += 1
        else:
            print("draw")

    print(name + " ["+ str(ps) + " : " + str(cs) + "] computer\n\n")
if ps > cs:
    print("\n\n\nCONGRATULATIONS, YOU WIN!!!")
else:
    print("YOU LOST!!")
