class employee:
    def __init__(self):
        self.ctc = int(input("Enter CTC: "))

    def caltax(self):
        if self.ctc <= 150000:
            print("No tax")
        elif 150000 < self.ctc <= 300000:
            self.taxper = 10
        elif 300000 < self.ctc <= 500000:
            self.taxper = 20
        else:
            self.taxper = 30

    def printinfo(self):
        self.tax = self.ctc * (self.taxper / 100)
        print(f"Tax = {self.tax}")
        print(f"income = {self.ctc - self.tax}")


e1 = employee()
e1.caltax()
e1.printinfo()
