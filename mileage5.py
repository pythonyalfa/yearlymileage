class Mileage:
    def __init__(self):
        self.miles = []

    def totalMiles(self):
        return sum(self.miles) * 2

    def computeTax(self, tax_rate = 0.59):
        return self.totalMiles() * tax_rate

    def addMileage(self, miles):
        if miles > 0:
            self.miles.append(miles)

if __name__ == '__main__':
    m = Mileage()
    miles = None

    while miles != 0:
        miles = float(input("Enter mileage one way (0 to exit and calculate total): "))
        m.addMileage(miles)

    print("Miles log", m.miles)
    print("Total miles driven this trip: ", m.totalMiles())
    print("Total tax credit this trip: ", m.computeTax())
