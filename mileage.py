#User enters mileage until they exit out of the program it will multiply times two and that total to the new total
#Lastly, it should multiple that total time .59 cents for tax purposes.

    


def cumulativeT(newTotal):
   list = [newTotal]
   #print (sum(list))
   print("Total miles: ",newTotal)
   print("Tax credit: ", newTotal * 0.58)
   


def addMileage(miles):
    
    total = miles 
    print("Total miles driven this trip: ",miles*2)
    print("Total tax credit this trip: ",miles * .58)
    cumulativeT(total)
    
   
  
 



def  test():
    
    while True:
        number = eval(input("Enter mileage one way (0 to exit and calculate total): "))
        if number == 0: break
    #cumulativeT(number) 
    
        else:
            addMileage(number)

test()
