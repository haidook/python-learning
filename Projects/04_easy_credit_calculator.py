import math
import argparse

parser = argparse.ArgumentParser(description='Helps you with your credit')
parser.add_argument("--type", help="type of payment")
parser.add_argument("--payment", type=int, help="the monthly payment")
parser.add_argument("--principal", type=int, help="the credit principal")
parser.add_argument("--periods", type=int, help="the number of months")
parser.add_argument("--interest", type=float, help="the interest rate")
args = parser.parse_args()

args_list = [args.payment, args.principal, args.periods, args.interest]

error = 'Incorrect parameters'

def check_negative():
    for v in args_list:
        if v != None and v < 0:
            return 0

def calc_diff_payments(a, b, c):
    i = (c / 100) / (12 * 100 / 100)
    m = 1
    suma = 0
    while m <= b:
        n = math.ceil((a / b) + i * (a - (a * (m - 1)) / b))
        print(f'Month {m}: paid out {n}')
        m += 1
        suma += n
    print('')
    print(f'Overpayment = {math.ceil(suma - a)}')

def calc_annuity_payment(a, b, c):
    i = (c / 100) / (12 * 100 / 100)
    n = math.ceil(a * ((i * (1 + i) ** b) / ((1 + i) ** b - 1)))
    # return n
    print(f'Your annuity payment = {n}!')
    print(f'Overpayment = {n * b - a}')

def calc_principal(a, b, c):
    i = (c / 100) / (12 * 100 / 100)
    n = math.floor(a / ((i * ((1 + i) ** b)) / (((1 + i) ** b) - 1)))
    print(f'Your credit principal = {n}!')
    print(f'Overpayment = {b * a - n}')

def calc_months(a, b, c):
    global n2
    i = (c / 100) / (12 * 100 / 100)
    n = round(math.log((b / (b - i * a)), 1 + i), 2)
    n2 = math.ceil(n)

def convert_months(a, b):
    years = int(n2 / 12)
    months = n2 % 12
    if years == 0:
        print(f'You need {months} months to repay this credit!')
    elif months == 0:
        if years == 1:
            print(f'You need {years} year to repay this credit!')
        else:
            print(f'You need {years} years to repay this credit!')
    else:
        print(
            f'You need {years} years and {months} months to repay this credit!')
    print(f'Overpayment = {n2 * b - a}')

while (args.type not in ['annuity', 'diff']) or \
      (args.type == 'diff' and args.payment != None) or \
      (args.interest == None) or \
      args_list.count(None) >= 2 or \
      check_negative() == 0:
    print(error)
    break

else:
    if args.type == 'diff':
        credit_principal = args.principal
        count_of_periods = args.periods
        credit_interest = args.interest
        calc_diff_payments(credit_principal, count_of_periods, credit_interest)
    elif args.type == 'annuity':
        if args.payment == None:
            credit_principal = args.principal
            count_of_periods = args.periods
            credit_interest = args.interest
            calc_annuity_payment(credit_principal, count_of_periods, credit_interest)
        elif args.principal == None:
            payments = args.payment
            count_of_periods = args.periods
            credit_interest = args.interest
            calc_principal(payments, count_of_periods, credit_interest)
        else:
            credit_principal = args.principal
            payments = args.payment
            credit_interest = args.interest
            calc_months(credit_principal, payments, credit_interest)
            convert_months(credit_principal, payments)