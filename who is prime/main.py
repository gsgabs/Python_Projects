
def prime_checker(number):
  isPrime = True
  if number == 1 or number == 2:
    print(f'{number} Is Prime')
  else:
    for n in range(2, number):
      if number % n == 0:
        isPrime = False
    if isPrime:
      print(f'{number}   Prime\n')
    elif not isPrime:
      print(f"{number}   Not  prime\n")

item = 1
while item < 100:
  prime_checker(item)
  item += 1
