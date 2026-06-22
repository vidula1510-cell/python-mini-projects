## Input we need from the user 
#Total rent
#Total food ordered for snacking
#Electricity units spend
#charge per unit
#persons living in flat

## Output
#Total amount you've to pay is

rent = int(input("Enter your flat rent = "))
food = int(input("Enter the amount of food order = "))
electricity_spend = int(input("Emtre the total of electricity spend = "))
charge_per_unit = int(input("Entre the charge per unit = "))
persons = int(input("Entre the number of persons living in the flat = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay = ",output)