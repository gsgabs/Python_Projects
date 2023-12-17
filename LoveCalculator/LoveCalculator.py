print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
total_true = 0
total_love = 0
verdade = 'true'
amor = 'love'

for i in range(len(verdade)):
  for t in range(len(name1)):
    if name1[t] == verdade[i]:
      total_true += 1
  for j in range(len(name2)):
    if name2[j] == verdade[i]:
      total_true += 1

for i in range(len(amor)):
  for t in range(len(name1)):
    if name1[t] == amor[i]:
      total_love += 1
  for j in range(len(name2)):
    if name2[j] == amor[i]:
      total_love += 1
true_love = str(total_true) + str(total_love)
true_love = int(true_love)
if true_love < 10 or true_love > 90:
  print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love > 40 and true_love < 50:
  print(f"Your score is {true_love}, you are alright together.")
else:
  print(f"Your score is {true_love}.")