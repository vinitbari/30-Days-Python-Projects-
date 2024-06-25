#import Library and give a alias name 
import pywhatkit as pw 

#add your custom text 
#we use triple code because we have to add whole para 

txt ="""" 
  
   Python is an interpreted high-level general-purpose 
   programming language. 
   Its design philosophy emphasizes code readability with its use of 
   significant indentation. """ 

#we will use inbuilt function 
#if we didn't give any name it will save by pywhatkit.png 
#we have to give three parameters : text , file name , color 
#by default color is blue 

pw.text_to_handwriting(txt) 
print ("Code is running")