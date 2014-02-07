import math

STARTING_BALANCE = float(raw_input('Please give the starting balance: '))
INTEREST_RATE = float(raw_input('Please give the annual interest'
                                'rate (decimal): '))

MONTHLY_INTEREST_RATE = INTEREST_RATE/12
balance = STARTING_BALANCE

monthly_payment_lower_bound = STARTING_BALANCE/12
monthly_payment_upper_bound = (STARTING_BALANCE *
                               (1 + MONTHLY_INTEREST_RATE)**12)/12


while (monthly_payment_upper_bound - monthly_payment_lower_bound) > 0.01 \
      or balance > 0:

    monthly_payment = (monthly_payment_lower_bound +
                       monthly_payment_upper_bound)/2
    
    balance = STARTING_BALANCE

    for month in range(1,13):
        interest = balance * MONTHLY_INTEREST_RATE
        balance += interest - round(monthly_payment,2)

        balance = round(balance,2)

        if balance < 0:
            break

    if balance > 0:
        monthly_payment_lower_bound = monthly_payment
    else:
        monthly_payment_upper_bound = monthly_payment

print 'Monthly payment to pay off debt in 1 year:', round(monthly_payment,2)
print 'Number of months needed: ', month
print 'Balance: ', balance

        

    
    
