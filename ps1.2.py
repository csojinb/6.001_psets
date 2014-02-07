STARTING_BALANCE = int(raw_input('Please give the starting balance: '))
INTEREST_RATE = float(raw_input('Please give the annual interest rate (decimal): '))

MONTHLY_INTEREST_RATE = INTEREST_RATE/12
balance = STARTING_BALANCE
payment_multiplier = 1
PAYMENT_INCREMENT = 0.01

while balance > 0:

    monthly_payment = payment_multiplier * PAYMENT_INCREMENT
    balance = STARTING_BALANCE
    # print 'Monthly payment:', monthly_payment

    for i in range(12):
        interest = balance * (MONTHLY_INTEREST_RATE)
        balance += interest - monthly_payment
        # print i, balance

        if balance < 0:
            break

    payment_multiplier += 1

print 'Monthly payment to pay off debt in 1 year:', monthly_payment
print 'Number of months needed:', i + 1
print 'Balance:', round(balance,2)