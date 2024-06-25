import string 
import random 

if __name__ =="__main__": 
 #Now we will creat a Empty list & Extend all values in one variable
 s1 = string.ascii_uppercase 
 s2 = string.ascii_lowercase 
 s3 = string.digits 
 s4 = string.punctuation 

# print(s1,s2,s3,s4) 
#Now we will creat a Empty list & Extend all values in one variable 
#remember there is a difference in append & Extend 

passwordlength = int(input("Enter the length of the password : \n")) 
s= [] 
s.extend(list(s1)) 
s.extend(list(s2)) 
s.extend(list(s3)) 
s.extend(list(s4)) 

#print (s) 
random.shuffle(s) 
print("".join(s[0:passwordlength]))