savings = int(input("enter the percentage of savings for this month: "))
rent = int(input("enter the percentage of rent for this month: "))
electricity = int(input("enter the percentage of electricity for this month: "))
month = ""

while month != "stop":
  salary = int(input("enter your salary: "))
  month = input("enter the month: ")
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

