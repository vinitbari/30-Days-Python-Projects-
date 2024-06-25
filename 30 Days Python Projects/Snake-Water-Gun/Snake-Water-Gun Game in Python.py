import random

def check (computer,user): 
  
  if (computer==user) : 
   return 0 
  if (computer==0 and user ==1 ) : 
   return -1 
  if(computer == 1 and user ==2) : 
   return -1 
  if(computer == 2 and user ==0) : 
   return -1 
   return 1 
  
user = int(input("0 for snake , 1 for water and 2 for gun ")) 

computer = print(random.randint(0,2)) 
score = check(computer , user ) 

print("computer : ",computer) 
print("user : ", user) 

if (score==0 ): 
   print ("Its a Draw !") 
elif score==-1: 
   print ("You Lose") 
else : 
   print("You Win") 