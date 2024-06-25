print("Calculator") 
num1=int(input("Enter First Number: ")) 
num2=int(input("Enter second Number:")) 
#Operations ! 

print ("press + for addition \n press - for substraction \n press * for Multiplication \n press / for Division") 

Choice=(input ("Enter Your operation from above ")) 

if Choice == '+' : 
 print(num1+num2) 
elif Choice == '-' : 
 print(num1-num2) 
elif Choice == '*' : 
 print(num1*num2) 
elif Choice == '/' : 
 print(num1/num2) 
else: 
 print("Enter a Valid Operator")