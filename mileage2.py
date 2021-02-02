def sum_list(l):
    
    
    sum = 0
    for x in l:
        sum += x
    return sum



def  test():

    while True:
    number = [] 
    number = float(input("Enter mileage one way (0 to exit and calculate total): "))

        
        if number == 0: break   
        
        else:
            number.append(int(number))
            sum_list(number)

test()
