#Prompts user to enter the amount spend monthly
spending_is_number = False
rate_is_number = False
save_invest_is_number = False

while spending_is_number == False:
    try:
        print("Please enter the amount you spend a month on average (Inclusive of Insurance, Rental, etc): ")
        monthly_spend = float(input("Enter here: "))
        spending_is_number = True
    except ValueError as err:
        print(err, "Please enter numbers only (For example: 1000).")

#Prompts user to enter the rate of return for their investments/savings
while rate_is_number == False:
    try:
        print("Please enter the rate of return on average (1 percent return : 0.01%): ")
        rate_of_return = float(input("Enter here: "))
        rate_is_number = True
    except ValueError as err:
        print(err, "Please enter decimal only (For example: 0.02).")

#Prompts user to enter the amount that they save/invest monthly then multiplies value by 12 to get annual savings/investments
while save_invest_is_number == False:
    try:
        print("How much do you save/invest a month on average (Inclusive of Savings Accounts, Investments, Bonds, etc)")
        amount_not_spent = float(input("Enter here: "))
        save_invest_is_number = True
    except ValueError:
        print("Please enter numbers only (For example: 3000).")

annual_spend = monthly_spend * 12
annual_amountnotspent = amount_not_spent * 12

#Calculates the amout of money to reach Financial Independence by taking the annual spend and dividing by the rate of returns
amount_to_reach_FI = annual_spend / rate_of_return

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