def __init__(self,stock): 
 self.stock=stock 

def displaybike(self): 
 print ("Total Bikes",self.stock) 

def rentforbike(self,q): 
 
 if q<=0: 
   print ("Enter the positive value or greater then zero") 
 elif q>self.stock: 
  print("Enter the value (Less then stock )") 
 else : 
    print("Total Prices ", q*100) 
    print("Total bikes ", self.stock) 

 while True: 
   obj=bikeshop(100) 
   uc=int(input('''
                1-Display Total Number of bikeshop 
                2-Rent a Bike 
                3-Exit 
                  ''')) 

   if uc==1: 
     obj.displaybike() 
   elif uc==2: 
     n=int(input("Enter Number of Bikes you want : " )) 
     obj.rentforbike(n) 
   else: 
     break 