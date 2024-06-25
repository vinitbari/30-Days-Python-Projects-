from time import time
def tperror(prompt): 
 global inwords
 words = prompt.split()
 error = 0
 for i in range(len(inwords)): 
  if i in (0, len(inwords)-1): 
   if inwords[i] == words[i]: 
     continue 
   else: 
    error += 1 
  else: 
   if inwords[i] == words[i]: 
    if (words[i-1]): 
      (inwords[i+1])
    continue 
 else: 
   error += 1 
 return error 

def calc_speed(inprompt, stime, etime): 
 global inwords
 inwords = inprompt.split()
 twords = len(inwords)
 speed = twords / (etime - stime) * 60
 return speed 
def elapsed_time(stime, etime):
 elapsed = etime - stime
 return elapsed 
if __name__ == '__main__': 
    prompt = ("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in  1991, Python's design philosophy emphasizes code readability with its  notable use of significant whitespace. Its language constructs and object oriented approach.") 
print("Type this:- ", prompt,"") 
input("Press Enter when you are ready to check your speed!!!") 
stime = time() 
inprompt = input() 
etime = time() 
elapsed = round(elapsed_time(stime, etime), 2) 
typing_speed = calc_speed(inprompt, stime, etime) 
errors = tperror(prompt) 
print("Total time elapsed:", elapsed, "seconds") 
print("Your Average Typing speed was", typing_speed, "words per minute (w/m)") 
print("with a total of", errors, "errors")