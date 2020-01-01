#Prompts user to enter the amount spend monthly then multiplies value by 12 to get annual spend
print("Please enter the amount you spend a month on average (Inclusive of Insurance, Rental, etc): ")
monthly_spend = input("Enter here: ")
annual_spend = float(monthly_spend) * 12

#Prompts user to enter the rate of return for their investments/savings
print("Please enter the rate of return on average (1 percent return : 0.01%): ")
rate_of_return = input("Enter here: ")

#Prompts user to enter the amount that they save/invest monthly then multiplies value by 12 to get annual savings/investments
print("How much do you save/invest a month on average (Inclusive of Savings Accounts, Investments, Bonds, etc)")
amount_not_spent = input("Enter here: ")
annual_amountnotspent = float(amount_not_spent) * 12

#Calculates the amout of money to reach Financial Independence by taking the annual spend and dividing by the rate of returns
amount_to_reach_FI = float(annual_spend) / float(rate_of_return)

#Calculates the years to reach Financial Independence by taking the amount to reach Financial Independence diving by Annual Spend
years_to_reach = amount_to_reach_FI / annual_amountnotspent
rounded_years = round(years_to_reach)

#Calculates the months and days to reach Financial Independence
months_to_reach = years_to_reach * 12
days_to_reach = round(years_to_reach * 365)

#Prints stuff
print("This is the amount you will save/invest in a year: ", annual_amountnotspent)
print("This is the amount you need to reach Financial Independence: ", amount_to_reach_FI)
print("This is the number of years you will take to reach Financial Independence: ", rounded_years)
print("This is the number of months you will take to reach Financial Independence: ", months_to_reach)
print("This is the number of days you will take to reach Financial Independence: ", days_to_reach)