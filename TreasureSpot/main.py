line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letra = position[0]
lower_letra = letra.lower()
if lower_letra == 'a':
  index = 0
if lower_letra == 'b':
  index = 1
if lower_letra == 'c':
  index = 2
numero = position[1]
numero = int(numero)
map[numero - 1][index] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")