def monthly_payment(balance,interest_rate,min_payment_rate):
    min_payment = balance * (1 + min_payment_rate)
    interest = balance * (1 + interest_rate/12)
    new_balance = balance + interest - min_payment
    return round(new_balance,2)

interest_rate = 0.2
min_payment_rate = 0.04
balance = 4800

for i in range(12):
    balance = monthly_payment(balance,interest_rate,min_payment_rate)
    print i + 1, balance

