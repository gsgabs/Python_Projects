import random
from replit import clear

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


# Declaração
life = 6
word_list = ["condensado", "vassoura", "banana", "corrida", "caramelo"]
word = random.choice(word_list)
blank_word = ''
for letter in word:
  blank_word += '_'
letras_erradas = []
  
print(f"Voce tem {life} vidas")
print(blank_word)

while blank_word != word and life > 0:
  letra_repetida = False
  guess = input("\n\nChute uma letra:\n")
  clear()
  guess = guess.lower()
  for letter in letras_erradas:
    if letter == guess:
      letra_repetida = True
  if letra_repetida == True:
    print(f"A letra {guess} ja foi utilizada, por favor insira uma letra diferente.")
  else:
    letras_erradas.append(guess)
    errou = True
    position = -1
    blank_list = list(blank_word)
    for letter in word:
      position += 1
      if guess == letter:
        blank_list[position] = guess
        errou = False
    if errou == True:
      print(f"\nA letra {guess} não está na palavra")
      life -= 1
    blank_word = ''
    for letter in blank_list:
      blank_word += letter
    print(blank_word)
    print(stages[life])
    print("Letras ja usadas: ")
    print(letras_erradas)
    

if life == 0:
  print("You Lose")
  print('G A M E   O V E R !')
elif blank_word == word:
  print("Congratulations You Won!")
  print('Game Over!')

