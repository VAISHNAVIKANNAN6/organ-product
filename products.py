#from category import Category 
#@classmethod
class Order: 
    def __init__(self,no): 
        self.no=no  
    def sleeping_mask(self): 
        print(self.no,"- you selected Beauty Calming Midnight sleeping Mask") 
        print ("only 1kg packet is available","\t1kg = 500") 
        total=int(input("how many items do you want")) 
        payment=total * 500 
        d=Details(payment) 
        d.address() 
    def hydrating_serum(self): 
        print(self.no,"- you selected Homemade Hydrating serum") 
        print ("only 1kg packet is available","\t1kg = 750") 
        total=int(input("how many items do you want")) 
        payment=total * 750 
        d=Details(payment) 
        d.address()        
    def makeup_remover(self): 
        print(self.no,"- you selected natural makeup remover ") 
        print ("only 1kg packet is available","\t1kg = 250") 
        total=int(input("how many items do you want")) 
        payment=total * 250 
        d=Details(payment)
        d.address() 
    def facial_scrub(self): 
        print(self.no,"- you selected unisex facial scrub") 
        print ("only 1kg packet is available","\t1kg = 600") 
        total=int(input("how many items do you want:")) 
        payment=total * 600 
        d=Details(payment) 
        d.address() 
    def organic_soap(self): 
        print(self.no,"- you selected organic soap") 
        print ("only 200g box are available","\t1box = 100") 
        total=int(input("how many items do you want:")) 
        payment=total * 100 
        d=Details(payment) 
        d.address() 
    def organic_shampoo(self): 
        print(self.no,"- you selected organic shampoo") 
        print ("only 200g bottle available","\t1kg = 100") 
        total=int(input("how many items do you want:")) 
        payment=total * 100 
        d=Details(payment) 
        d.address() 
    def tulsi(self): 
        print(self.no,"- you selected tulsi iced tea powder(mix it in hot water)") 
        print ("only 1kg packets are available","\t1kg = 400") 
        total=int(input("how many items do you want:")) 
        payment=total * 400 
        d=Details(payment) 
        d.address(payment) 
    def buckwheat(self): 
        print(self.no,"- you selected buckwheat  ") 
        print ("only 1kg packets are available","\t1kg = 300") 
        total=int(input("how many items do you want:")) 
        payment=total * 300 
        d=Details(payment) 
        d.address() 
    def ginger(self): 
        print(self.no,"- you selected ginger chai powder") 
        print ("only 1kg packets are available","\t1kg = 500") 
        total=int(input("how many items do you want:")) 
        payment=total * 500 
        d=Details(payment) 
        d.address() 
    def maple_water(self): 
        print(self.no,"- you selected maple water") 
        print ("only 1kg packets are available","\t1kg = 500") 
        total=int(input("how many items do you want:")) 
        payment=total * 500 
        d=Details(payment) 
        d.address() 
    def manure(self): 
        print(self.no,"- you selected manure") 
        print ("only 1kg packets are available","\t1kg = 500") 
        total=int(input("how many items do you want:")) 
        payment=total * 500 
        d=Details(payment) 
        d.address() 
    def vermicompost(self): 
        print(self.no,"- you selected vermicompost") 
        print ("only 1kg packets are available","\t1kg = 1000") 
        total=int(input("how many items do you want:")) 
        payment=total * 1000 
        d=Details(payment) 
        d.address() 
    def chickenlitter(self): 
        print(self.no,"- you selected chickenlitter") 
        print ("only 1kg packets are available","\t1kg = 700") 
        total=int(input("how many items do you want:")) 
        payment=total * 700 
        d=Details(payment) 
        d.address()       
#@classmethod
class Details: 
    def __init__(self,payment): 
        self.payment=payment 
    def address(self): 
        q2=input("Enter your Name : ") 
        q3=input("Enter your Address : ") 
        q4=int(input("Enter your mobile no: ")) 
        print("Thanks for ordering",q2) 
        print("\nthe selected organic product will be deliver soon to",q3) 
        print ("\nif any queries ...contact customer care via your registered phone number",q4) 
        print ("""only cash on delivery available 
                  total amount to be paid:""",self.payment)