import random

def generate_response(user_input):
  responses = [
    "How interesting!",
    "You don't say!",
    "Very cool!",
    "Programming is fun!"
  ]
  return random.choice(responses)


def initial_chat():
  input("Hi my name name is Kevin and I will be chatting with you today!! \n(Press enter to continue) \n")
  user_name = input("First, what is your name?\n")
  input(f'Nice to meet you {user_name}!\n(Type in "q" to quit)\n')
  user_response = input("How are you doing? \n")
  
  
  while user_response != "q":
    user_response = input(generate_response(user_response)+ "\n")
    
    
  print("Thanks for chatting")
initial_chat()