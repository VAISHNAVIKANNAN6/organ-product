import sys  
from category import Category 
def order_menu():                                                                              
    while True:                                             
        print("" * 31 + "CATEGORY" + "" * 31 + "\n"    
              "\t(S) SKIN CARE PRODUCTS\n" 
              "\t(D) DRINKS\n" 
              "\t(F) FERTILIZERS \n" 
               "\t(E) EXIT \n" + "_" * 72) 
        input_1 = str(input("Please Select Your Operation: ")).upper()  
        o1=Category(input_1) 
        if len(input_1) == 1: 
            if (input_1 == 'S'): 
                print("\n" * 10) 
                o1.skin_care_products()  
                break 
            elif (input_1 == 'D'): 
                print("\n" * 10) 
                o1.drinks() 
                break 
            elif (input_1 == 'F'): 
                print("\n" * 10) 
                o1.fertilizers()  
                break  
            elif (input_1 == 'E'): 
                sys.exit() 
            else:                
               print("Invalid input") 
        else: 
            print("Invalid nput")        
 

 
 