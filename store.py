import datetime


class store:
    quantity = 0
    purchased = False

    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price


p = []
num = 5
p.append(store("Shirt", int(1), int(40)))
p.append(store("Jeans", int(2), int(50)))
p.append(store("Shoes", int(3), int(70)))
p.append(store("Jacket", int(4), int(90)))
p.append(store("Belt", int(5), int(20)))

run = True
productnotFound = True

cname = input("Enter your name: ")

while (run):
    productnotFound = True
    print("\nProduct:\t|\tcode:\t|\tPrice:")
    for i in range(num):
        print("------------|-----------|-----------")
        print(f"\t{p[i].name}\t|\t{p[i].code}\t\t|\t${p[i].price}")

    c = int(input("\n(ENTER '0' TO EXIT)\n\nEnter code of product you want to purchase: "))

    for i in range(num):
        if c == p[i].code:
            productnotFound = False
            p[i].quantity = int(input("Enter quantity: "))
            if p[i].quantity > 0:
                p[i].purchased = True

    if productnotFound:
        print("Invalid code!\n")

    if c == 0:
        print(f"\nThank you {cname}, for shopping here!")
        run = False

date = datetime.date.today()
time = datetime.datetime.now().time()

total = 0
for i in range(num):
    total += p[i].price * p[i].quantity
print("----------------- BILL --------------")
print(f"Name : {cname}\nDate : {date}\nTime : {time}\n")
print("__________________________")
print("Product\t|\tqty\t|\tprice")
print("--------|-------|---------")
for i in range(num):
    if p[i].purchased:
        print(f"{p[i].name}\t|\t {p[i].quantity}\t|\t${p[i].quantity * p[i].price}")

print(f"\n\nTotal: ${total}\n")
print("-----------------X--X--X--------------")
