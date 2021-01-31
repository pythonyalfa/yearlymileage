#User enters mileage until they exit out of the program it will multiply times two and that total to the new total
#Lastly, it should multiple that total time .59 cents for tax purposes.

def total(total):
    print(total)

def tax(addTax):
    addedall = 0
    addedall += addTax
    total(addedall)

def cumulativeT(newTotal):
   print("Total miles: ",newTotal)
   print("Tax credit: ", newTotal * 0.58)
   tax(newTotal)

def addMileage(miles):
    
    total = miles * 2 
    print("Total miles drive this trip: ",total)
    cumulativeT(total)
    answer = input("Would like to finish? (Please only y or n) ")
    if answer == "n":
           test()
    if answer == "y":
           cumulativeT(total)
           total(total)
def  test():
    
    while True:
        
        number = eval(input("Enter mileage one way (0 to exit and calculate total): "))
       
        if number == 0: break   
        
        else:
            addMileage(number)

test()
