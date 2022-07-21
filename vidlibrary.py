import datetime


class vidlib:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.oldmov = int(input("Enter number of days for old movie: "))
        self.newvids = int(input("Enter number of days for new movie: "))

    def billing(self):
        date = datetime.date.today()
        time = datetime.datetime.now().time()
        totalbill = (self.oldmov * 50) + (self.newvids * 75)
        print("\n\n----------------- BILL --------------")
        print(f"Name : {self.name}\nDate : {date}\nTime : {time}\n")
        print("_______________________________")
        print("Product\t\t|\tday\t|\tprice/day")
        print("------------|-------|---------")
        print(f"old movie\t|\t {self.oldmov}\t|\t$50")
        print(f"new movie\t|\t {self.newvids}\t|\t$75")
        print(f"\nTotal: ${totalbill}")
        print("-----------------X--X--X--------------")


v1 = vidlib()
v1.billing()
