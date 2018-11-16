import random

def mini_game(a,b):
  health_points=3
  guess= input("Guess the number bimbo:")
  secret_number= random.randint(a,b)
if guess>!=secret_number:
  return ("Woah buddy, too high.")
elif guess<!=secret_number:
  ("Well someone's down in the dumps, that's a pretty low number.")
if guess==secret_number:
  print("Yay you guessed it!")
  print("Level 2!")
elif health_points>0:
  print("haha stupid, you lost a life :)))")
  lives = lives-1
  secret_2= random.randint(a,b+5)
  guess_2= input("Round 2!")


  if guess_2==secret_2:
    print("Two in a row!")
    print ("Level 3!")
  else:
    print("Who are you again?")
    secret_3= (a,b+5)
    guess_3= ("Round 3!")
  if guess_2>!=secret_2:
  return ("Woah buddy, too high.")
elif guess_2<!=secret_2:
  print ("Someone's down in the dumpster, too low.")
  
    if guess==secret_3:
      print("YOU WON!!! HAVE A COOKIE")
else: health_points == 0:
  print("Game over")
  if guess_3>!=secret_3:
  return ("Woah buddy, too high.")
elif guess_3<!=secret_3:
  print ("Ya missed, too low. Cheer up buddy.")

