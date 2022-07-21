class series:
    def __init__(self):
        self.fro = int(input("Enter starting point of series: "))
        self.to = int(input("Enter end point of series: "))
        self.inc = int(input("Enter increment: "))

    def putseries(self):
        i = self.fro
        print()
        while i <= self.to:
            print(str(i), end=",")
            i += self.inc
        print("\b")


s = series()
s.putseries()
