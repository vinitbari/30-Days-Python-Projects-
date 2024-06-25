import random

print("Welcome to the Guessing Game")

print("I am thinking of a number between 1 and 100")

print("Try to guess the number in the least number of guesses")

print("Good Luck")

computer=random.randrange(1,100)

 #randrange is use to define a range for computer to choose a random number
 # computer to choose   a random number 

user=int(input("Enter your number : \n")) 

#Comperision 
if user>computer: 
  print("computer : ",computer) 
  print("Your Guess number is too High") 
elif computer>user: 
  print("computer number : " , computer ) 
  print("Your Guess number is too Low ") 
else: 
  print ("Computer number : " ,computer) 
  print("Your Guess number is equal ! You win !!") 

#we can make this game more difficult ! by increasing range