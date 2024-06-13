#Task 1
peanut_butter = 10
jelly = 20
bread = 30

price_per_sandwich = (peanut_butter / 8) + (jelly / 8) + (bread / 6)

print(price_per_sandwich)

#Task 2
account_balance = 10000
interest_rate = .07
years_to_simulate = 200

for year in range(years_to_simulate):
    yearly_accrual = account_balance * interest_rate
    account_balance += yearly_accrual

print('Account Balance after ' + str(years_to_simulate) + ' years: ' + str(account_balance) )

