#User enters mileage until they exit out of the program it will multiply times two and that total to the new total
#Lastly, it should multiple that total time .59 cents for tax purposes.

    


def cumulativeT(newTotal):
   tot = [newTotal]
   l = 0.0
   #tot.append(l)

   print (tot)
   
   #print("Total miles: ", total)
   #print("Total tax credit: ", total * .58)
    


def addMileage(miles):
    
    total = miles * 2 
    
    print("Total miles driven this trip: ",total)
    print("Total tax credit this trip: ",total * .58)
    cumulativeT(total)
    
   
  
 



def  test():
    
    while True:
        number = eval(input("Enter mileage one way (0 to exit and calculate total): "))
        
       

      
     
        
        addMileage(number)
        
        if number == 0: break
                 
            

test()
