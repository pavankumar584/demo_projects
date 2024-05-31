# Calculating electrical bill using the python programming

# 1 to 100 units - 1.5Rs
# 101 to 200 units - 2.5Rs
# 201 to 300 units - 4Rs
# 300 to 350 units - 5Rs
# Above 350 - Fixed charge 1500Rs

try:
    units = float(input("Enter the Unit Consumed: "))
    if units <= 0:
        raise ValueError("Unit consumed should be a positive value.")
except ValueError:
    print("Invalid input. Please enter a positive numeric value for units consumed.")
    exit()

if units > 0 and units <= 100:
    payment = units * 1.5
    fixedCharge = 25  # Extra charge
elif units > 100 and units <= 200:
    payment = (100 * 1.5) + (units - 100) * 2.5
    fixedCharge = 50  # Extra charge
elif units > 200 and units <= 300:
    payment = (100 * 1.5) + (200 - 100) * 2.5 + (units - 200) * 4
    fixedCharge = 75  # Extra charge
elif units > 300 and units <= 350:
    payment = (100 * 1.5) + (200 - 100) * 2.5 + (300 - 200) * 4 + (units - 300) * 5
    fixedCharge = 100  # Extra charge
else:
    payment = 0
    fixedCharge = 1500

total = payment + fixedCharge
print(f"Your Electricity Bill amount is {total:.2f}")