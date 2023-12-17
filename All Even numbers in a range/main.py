target = int(input()) # Enter a number between 0 and 1000

if target < 0:
  target *= -1
total = 0
for i in range(2, (target + 1), 2):
  total += i
print(total)