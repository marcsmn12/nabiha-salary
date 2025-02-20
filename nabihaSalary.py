# Nabiha, a software engineering consultant, receives a variable salary every month. She wants to create a Python script that helps her manage her monthly finances by calculating how much money will be allocated to different categories like savings, rent, and electricity, based on percentages of his salary.

# Your task is to write a Python script that automates these calculations. The script should:


# • Ask Nabiha to input her salary for the month.
# • Ask Nabiha to input the name of the month she is storing the salary for.
# • Ask Nabiha to input the following percentages for: a) Savings b) Rent c) Electricity

# The script should calculate and display:


# • The amount allocated to savings, rent, and electricity.
# • The total amount Nabiha spends on savings, rent, and electricity combined.
# • The remainder of Nabiha’s salary after these expenses.
# • The monthly rent and electricity multiplied by 12 to estimate Nabiha's yearly rent and electricity costs.
# • Nabiha's total salary for the month raised to the power of 2 (just for fun).
# • Assume Nabiha saves an additional random amount (e.g., $50) each month, and you need to calculate how much would be left if this amount is divided by the total amount allocated to savings.

# Finally, the script should output all the results in a readable format. 

salary = int(input("enter your salary: "))
month = input("enter the month: ")
savings = int(input("enter the percentage of savings for this month: "))
rent = int(input("enter the percentage of rent for this month: "))
electricity = int(input("enter the percentage of electricity for this month: "))

amount_savings = salary * (savings / 100)
amount_rent = salary * (rent / 100)
amount_electricity = salary * (electricity / 100)
total_amount = amount_savings + amount_rent + amount_electricity
remainder = salary % total_amount
yearly_rent = amount_rent * 12
yearly_electricity = amount_electricity * 12
salary_raisedbytwo = salary ** 2

print(f"The amount allocated for savings is {amount_savings}")
print(f"The amount allocated for rent is {amount_rent}")
print(f"The amount allocated for electricity is {amount_electricity}")
print(f"The total amount spent on savings, rent, and electricity is {total_amount}")
print(f"The remainder of your salary after the expenses is {remainder}")
print(f"Your yearly rent cost is {yearly_rent}")
print(f"Your yearly electricity cost is {yearly_electricity}")
print(f"Your salary raised to the power of 2 is {salary_raisedbytwo}")

