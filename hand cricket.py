# hand cricket
import random


def playerbat(cs):
    print("\n\n\n\n\nyour chance to bat:")
    p = 0
    c = 1
    ps = 0

    while p != c and ps <= cs:
        p = 0

        while p > 6 or p < 1:
            p = int(input("\nenter choice (1 to 6)"))

        c = random.randint(1, 6)
        print("computer: " + str(c))
        if c == p:
            print("\nOUT!\nYour score: " + str(ps))
        else:
            ps += p
            print("\nYour score: " + str(ps))
    return ps


def playerbowl(ps):
    print("\n\n\n\n\nyour chance to bowl:")
    p = 0
    c = 1
    cs = 0


    while p != c and cs <= ps:
        p = 0

        while p > 6 or p < 1:
            p = int(input("\nenter choice (1 to 6)"))

        c = random.randint(1, 6)
        print("computer: " + str(c))
        if c == p:
            print("\nOUT!\ncomputer score: " + str(cs))
        else:
            cs += c
            print("\ncomputer score: " + str(cs))
    return cs


p = 0
c = 1
ps = 0
cs = 0
toss = int(input("heads or tails? [H=1/T=2]"))
coin = random.randint(1, 2)

if coin == toss:
    choice = int(input("\nyou won the toss!\nbat=1\tbowl=2"))

else:
    print("\nyou lost the toss!")
    choice = random.randint(1, 2)

if choice == 1:
    ps = playerbat(1000)
    print("\n\n\ntarget: " + str(ps + 1))
    cs = playerbowl(ps)

    if ps > cs:
        print("you win by " + str(ps - cs) + " runs!!")

    elif cs > ps:
        print("you lost by " + str(cs - ps) + " runs!!")

    else:
        print("draw!!")

else:
    cs = playerbowl(1000)
    print("\n\n\ntarget: " + str(cs + 1))
    ps = playerbat(cs)

    if ps > cs:
        print("\n\n\tyou win by " + str(ps - cs) + " runs!!")

    elif cs > ps:
        print("\n\n\tyou lost by " + str(cs - ps) + " runs!!")

    else:
        print("\n\n\tdraw!!")
