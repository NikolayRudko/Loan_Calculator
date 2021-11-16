import math
import argparse


def calculate_number_payments(loan_principal, monthly_payment, loan_interest):
    nominal_interest_rate = loan_interest / (12 * 100)
    base = 1 + nominal_interest_rate
    x = monthly_payment / (monthly_payment - nominal_interest_rate * loan_principal)
    months = math.ceil(math.log(x, base))
    years = int(months // 12)
    if months // 12 == 0:
        print('\nIt will take %d %s to repay the loan' % (months, 'months' if months > 1 else 'month'))
    elif months % 12 == 0:
        print('It will take %d %s to repay this loan!' % (years, 'year' if years > 1 else 'years'))
    else:
        print('It will take %d %s and %d %s to repay this loan!' %
              (years, 'years' if years > 1 else 'year', months % 12, 'months' if months > 1 else 'month'))
    total_sum = monthly_payment * months
    overpayment = total_sum - loan_principal
    overpayment = math.ceil(overpayment)
    print(f'Overpayment = {overpayment}')


def calculate_month_payment(loan_principal, number_periods, loan_interest):
    nominal_interest_rate = loan_interest / (12 * 100)
    base = 1 + nominal_interest_rate
    x = math.pow(base, number_periods)
    annuity_payment = (nominal_interest_rate * loan_principal * x) / (x - 1)
    annuity_payment = math.ceil(annuity_payment)
    print(f'Your monthly payment = {annuity_payment}!')
    overpayment = annuity_payment * number_periods - loan_principal
    overpayment = math.ceil(overpayment)
    print(f'Overpayment = {overpayment}')


def calculate_loan_principal(annuity_payment, number_periods, loan_interest):
    nominal_interest_rate = loan_interest / (12 * 100)
    loan_principal = annuity_payment / \
                     ((nominal_interest_rate * math.pow(1 + nominal_interest_rate, number_periods)) /
                      (math.pow(1 + nominal_interest_rate, number_periods) - 1))
    loan_principal = math.floor(loan_principal)
    # loan_principal = math.ceil(loan_principal)
    print(f'Your loan principal = {loan_principal}!')
    total_sum = annuity_payment * number_periods
    overpayment = total_sum - loan_principal
    overpayment = math.ceil(overpayment)
    print(f'Overpayment = {overpayment}')


def differentiated_payment(loan_principal, number_periods, loan_interest):
    nominal_interest_rate = loan_interest / (12 * 100)
    total_sum = 0
    for i in range(1, number_periods + 1):
        month_differentiated_payment = loan_principal / number_periods + nominal_interest_rate \
                                       * (loan_principal - (loan_principal * (i - 1)) / number_periods)
        month_differentiated_payment = math.ceil(month_differentiated_payment)
        print(f'Month {i}: payment is {month_differentiated_payment}')
        total_sum += month_differentiated_payment
    overpayment = total_sum - loan_principal
    overpayment = math.ceil(overpayment)
    print(f'\nOverpayment = {overpayment}')


def go():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type')
    parser.add_argument('--principal')
    parser.add_argument('--periods')
    parser.add_argument('--interest')
    parser.add_argument('--payment')
    args = parser.parse_args()

    if args.type == 'diff':
        if args.principal is not None and args.periods is not None and args.interest is not None:
            principal = float(args.principal)
            periods = int(args.periods)
            interest = float(args.interest)
            differentiated_payment(loan_principal=principal, number_periods=periods, loan_interest=interest)
        else:
            print('Incorrect parameters.')
    elif args.type == 'annuity':
        if args.principal is not None and args.periods is not None and args.interest is not None:
            principal = float(args.principal)
            periods = int(args.periods)
            interest = float(args.interest)
            calculate_month_payment(loan_principal=principal, number_periods=periods, loan_interest=interest)
        elif args.payment is not None and args.periods is not None and args.interest is not None:
            payment = float(args.payment)
            periods = int(args.periods)
            interest = float(args.interest)
            calculate_loan_principal(annuity_payment=payment, number_periods=periods, loan_interest=interest)
        elif args.principal is not None and args.payment is not None and args.interest is not None:
            principal = float(args.principal)
            payment = float(args.payment)
            interest = float(args.interest)
            calculate_number_payments(loan_principal=principal, monthly_payment=payment, loan_interest=interest)
        else:
            print('Incorrect parameters.')


go()