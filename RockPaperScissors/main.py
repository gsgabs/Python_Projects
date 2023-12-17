import random, my_function

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player_input = int(input('Type 0 for Rock, 1 for Paper or 2 for scissors: '))
aux = random.randint(0, 2)

if player_input == 0:
  player_choice = rock
if player_input == 1:
  player_choice = paper
if player_input == 2:
  player_choice = scissors

if aux == 0:
  bot_choice = rock
if aux == 1:
  bot_choice =paper
if aux == 2:
  bot_choice = scissors

print(player_choice)
print("Computer choose:")
print(bot_choice)

print(my_function.winner(player_input, aux))
