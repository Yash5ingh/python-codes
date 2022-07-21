riddhi = 0
yash = 0
choti = 0
score = 0

while True:
    score = int(input("Enter points: "))

    winner = input("Enter winner: ")
    if winner == 'y':
        yash += score
    if winner == 'c':
        choti += score
    if winner == 'r':
        riddhi += score

    listA = {
        yash: "Yash",
        riddhi: "Riddhi",
        choti: "Choti"
    }

    print(list)
