import sys 

no_of_categories = 0
salary_category = 0
interest_earn_afteroneyear = 0
amount_after_oneyear = 0
available_balance_validation = False
total_transactions_validation = False
credit_card_validation = False
home_loan_validation = False
insurance_policy_validation = False
investments_validation = False


print("Welcome to the DBS Multipler Account Calculator!\n")

while available_balance_validation == False:
    try:
        available_balance = float(input("Please enter available balance in your Multipler Account: "))
        available_balance_validation = True
    except ValueError as err:
        print(err, "Please enter numbers only. For example: 1000.")

#print(available_balance)

credit_salary = input("Do you credit your Salary into a DBS/POSB Bank Account? ")
if (credit_salary == "yes"):
    salary_category += 1 
else:
    print("You must credit your monthly salary into a DBS/POSB Account as it is the requirement.")
    sys.exit()
while total_transactions_validation == False:
    try:    
        total_transactions = float(input("Please enter the average total transactions you make in a month (inclusive of Salary Credit): "))
        total_transactions_validation = True
    except ValueError as err:
        print(err, "Please enter numbers only. For example: 10000")

while credit_card_validation == False:
    credit_card_spent = input("Do you transact in credit card spent with a DBS/POSB Credit Card? ")
    if (credit_card_spent == "yes"):
        no_of_categories += 1
        credit_card_validation = True
    elif(credit_card_spent == "no"):
        credit_card_validation = True
    else:
        print("Please enter either yes or no.")

while home_loan_validation == False:
    home_loan_investments = input("Do you take up any form of Home Loan Instalments? ")
    if (home_loan_investments == "yes"):
        no_of_categories += 1
        home_loan_validation = True
    elif(home_loan_investments == "no"):
        home_loan_validation = True
    else:
        print("Please enter either yes or no.")

while insurance_policy_validation == False:
    insuring_with_dbsposb = input("Do you have any Insurance Policy with DBS/POSB? (For example: ManuProtect MoneyBack.) ")
    if (insuring_with_dbsposb == "yes"):
        no_of_categories += 1
        insurance_policy_validation = True
    elif (insuring_with_dbsposb == "no"):
        insurance_policy_validation = True
    else:
        print("Please enter either yes or no.")

while investments_validation == False:
    investments_with_dbsposb = input("Do you have any investments with DBS/POSB? For example: Unit Trusts with DBS/POSB. ") 
    if (investments_with_dbsposb == "yes"):
        no_of_categories += 1
        investments_validation = True
    elif (investments_with_dbsposb == "no"):
        investments_validation = True
    else:
        print("Please enter either yes or no.")

if no_of_categories == 1:
    if total_transactions < 2000:
        rate_of_interests = 0.005
    elif 2000 <= total_transactions < 2500:
        rate_of_interests = 0.0155
    elif 2500 <= total_transactions < 5000:
        rate_of_interests = 0.0185
    elif 5000 <= total_transactions < 15000:
        rate_of_interests = 0.019
    elif 15000 <= total_transactions < 30000:
        rate_of_interests = 0.02
    else:
        rate_of_interests = 0.0208

if no_of_categories == 2:
    if total_transactions < 2000:
        rate_of_interests = 0.005
    elif 2000 <= total_transactions < 2500:
        rate_of_interests = 0.0180
    elif 2500 <= total_transactions < 5000:
        rate_of_interests = 0.02
    elif 5000 <= total_transactions < 15000:
        rate_of_interests = 0.022
    elif 15000 <= total_transactions < 30000:
        rate_of_interests = 0.023
    else:
        rate_of_interests = 0.035

if no_of_categories >= 3:
    if total_transactions < 2000:
        rate_of_interests = 0.005
    elif 2000 <= total_transactions < 2500:
        rate_of_interests = 0.02
    elif 2500 <= total_transactions < 5000:
        rate_of_interests = 0.022
    elif 5000 <= total_transactions < 15000:
        rate_of_interests = 0.024
    elif 15000 <= total_transactions < 30000:
        rate_of_interests = 0.025
    else:
        rate_of_interests = 0.038    

if available_balance > 50000:
    rate_of_interests = rate_of_interests + 0.005
    print("New Rate of Interest: ", str(rate_of_interests))


interest_earn_afteroneyear = rate_of_interests * available_balance
amount_after_oneyear = interest_earn_afteroneyear + available_balance
        


#print(credit_salary)
print("No of Categories: " , str(no_of_categories))
print("Rate of interest earned based on no. of categories" , str(rate_of_interests))
print("Amount of interest earned after a year" , str(interest_earn_afteroneyear))
print("Total Balance after a year with Multipler Account: " , str(amount_after_oneyear))




