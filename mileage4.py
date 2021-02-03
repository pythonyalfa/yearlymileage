def add_mileage(miles):
    total = miles * 2
    print("Total miles driven this trip: ", total)
    print("Total tax credit this trip: ", total * .58)
    return total



def test():
    while True:
        
        number = eval(input("Enter mileage one way (0 to quit)"))


        total = add_mileage(number)


        if total == 0: break


test()
