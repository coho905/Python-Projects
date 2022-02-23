import random
number = 0
win = False
level = int(input("Level 1, 2, or 3? "))
if level==1:
  number = random.randint(0,10)
  for i in range(0,5):
    guess = int(input("Guess: "))
    if number == guess:
      print("Good Job Champ")
      win = True
      break
    elif guess > number:
      print("Too High")
    elif number > guess:
      print("Too Low")
elif level==2:
  number = random.randint(0,100)
  for i in range(0,5):
    guess = int(input("Guess: "))
    if number == guess:
      print("Good Job Champ")
      win = True
      break
    elif guess > number:
      print("Too High")
    elif number > guess:
      print("Too Low")
elif level==3:
  number = random.randint(0,1000)
  for i in range(0,5):
    guess = int(input("Guess: "))
    if number == guess:
      print("Good Job Champ")
      win = True
      break
    elif guess > number:
      print("Too High")
    elif number > guess:
      print("Too Low")
if win == False:
  print("Better Luck Next Time")
