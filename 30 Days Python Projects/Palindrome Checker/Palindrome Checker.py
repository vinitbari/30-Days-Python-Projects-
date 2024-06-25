#Here we are taking input on which we have to check
# Are used for comments in python 

s= input("Enter the Value : \n ") 

 #Reverse function 
 #There are alot of methods for reversing 
 #but we are using slicing method 

reverse = s[::-1] 

if (s==reverse): 
  print("Yes it is a palindrome") 
else : 
  print("No it is not a palindrome")