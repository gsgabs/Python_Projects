#tip-calculator-end

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = float(input("How much tip would u like to give? 10, 15, 20? "))
total = total + (total * tip / 100)
people = float(input("How many people to split the bill? "))
total = round(total/people, 2)
total = format(total, ".2f")
print(f"Each person should pay: ${total}")







