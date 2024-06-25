from tkinter import * 
import random 

def random_computer_choice(): 
 return random.choice(['rock', 'paper', 'scissors']) 

def result(human_choice, comp_choice): 
 global user_score 
 global comp_score 
 
 if human_choice == comp_choice: 
  print("Tie") 
 elif (human_choice == "rock" and comp_choice == "scissors") or (human_choice == "paper" and comp_choice == "rock") or (human_choice == "scissors" and comp_choice == "paper"): 
  print("You Win") 
  user_score += 1 
 else: 
  print("Computer wins") 
  comp_score += 1 
 def rock(): 
  global user_choice 
  global comp_choice 
  user_choice = "rock" 
  comp_choice = random_computer_choice() 
  result(user_choice, comp_choice) 
 def paper(): 
  global user_choice 
  global comp_choice 
  user_choice = "paper" 
  comp_choice = random_computer_choice() 
  result(user_choice, comp_choice) 
 def scissors(): 
  global user_choice 
  global comp_choice 
  user_choice = "scissors" 
  comp_choice = random_computer_choice() 
  result(user_choice, comp_choice) 
# Create the Tkinter window 
  rps = Tk() 
  rps.geometry("300x300") 
  rps.title("Rock Paper Scissors") 
# Initialize scores 
  user_score = 0 
  comp_score = 0 
# Create buttons for each choice