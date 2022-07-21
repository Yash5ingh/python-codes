import random


def goalchance(t):
    print("\nGOAL CHANCE!!")
    shoot = int(input("shoot!\nleft=1\tright=2"))
    save = random.randint(1, 2)
    print("Computer: " + str(save))
    if shoot == save:
        print("\nSaved!")
        return 0
    else:
        print("\nGOALL!!!")
        pr.append(t)
        return 1


def save(t):
    print("\nGOAL CHANCE!!")
    shoot = int(input("Dive to block!\nleft=1\tright=2"))
    save = random.randint(1, 2)
    print("Computer: " + str(save))
    if shoot == save:
        print("\nGreat save!!")
        return 0
    else:
        print("\nGOALL!!!")
        cr.append(t)
        return 1


pos = True
time = 0
c = 1
p = 0
ps = 0
cs = 0
lim = int(input("Enter match length: "))
toss = int(input("heads or tails? [H=1/T=2]"))
coin = random.randint(1, 2)
pr = []
cr = []
if coin == toss:
    choice = int(input("\nyou won the toss!\ndo you want the ball?\n[yes=1 , no=2]"))

else:
    print("\nyou lost the toss!")
    choice = random.randint(1, 2)

if choice == 2:
    pos = False

while time <= lim:

    if pos:
        print("\n\n\n\n\n\n\n\n\n\n\n\nyou have the ball: ")
        d = 0
        p = 0
        c = 1
        while p != c and d < 3:
            print("\ntime: " + str(time) + "\nplayer " + str(ps) + " : " + str(cs) + " computer")
            print("players to dribble: " + str(3 - d))
            p = int(input("run:\nleft=1\tmiddle=2\tright=3"))
            c = random.randint(1, 3)
            print("computer: " + str(c))
            time += 1
            if p != c:
                d += 1
            else:
                pos = not pos
                break
            if d == 3:
                print("\n\ntime: " + str(time) + "\nplayer " + str(ps) + " : " + str(cs) + " computer")
                ps += goalchance(time)
                time += 1
                pos = not pos
                break

    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\ncomputer has the ball: ")
        d = 0
        p = 0
        c = 1
        while p != c and d < 3:
            print("\ntime: " + str(time) + "\nplayer " + str(ps) + " : " + str(cs) + " computer")
            print("defenders left: " + str(3 - d))
            p = int(input("tackle:\nleft=1\tmiddle=2\tright=3"))
            c = random.randint(1, 3)
            print("computer: " + str(c))
            time += 1
            if p != c:
                d += 1
            else:
                pos = not pos
                break
            if d == 3:
                print("\n\ntime: " + str(time) + "\nplayer " + str(ps) + " : " + str(cs) + " computer")
                cs += save(time)
                time += 1
                pos = not pos
                break

print("\n\n\n\n\n\n\n\nfull time!!\n\n\n\n\nplayer " + str(ps) + " : " + str(cs) + " computer")
print("goals time:\n" + str(pr) + "\t" + str(cr))
if ps > cs:
    print("\n\tYOU WIN!!!")
elif cs > ps:
    print("\n\tYOU LOSE!")
else:
    print("\n\tDraw!")
