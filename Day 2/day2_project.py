# A tip calculator which will tell you exactly how much you have to pay based on given information.

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

should_pay = (bill + (bill * (percentage/100))) / people
final_amount = "{:.2f}".format(should_pay)
print(f"Each person should pay: ${final_amount}")
