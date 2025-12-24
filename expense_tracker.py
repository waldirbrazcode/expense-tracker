import json
import datetime
import os
import random
from prettytable import PrettyTable

def add_expense(args):
    amount = args.amount
    desc = args.desc
    expenses = load_expenses()

    expense = {
        'id': len(expenses) + int(10000 * random.random()),
        'amount': amount,
        'desc': desc,
        'creation_date': datetime.datetime.now().strftime('%d/%m/%y'),
        'month_creation': int(datetime.datetime.now().strftime('%m')),
        'year_creation': int(datetime.datetime.now().strftime('%Y'))
    }

    expenses.append(expense)

    with open('expenses.json', 'w') as f:
        json.dump(expenses, f)

def delete_expense(args):
    expenses = load_expenses()
    expense_id = args.id

    for expense in expenses:
        if expense['id'] == expense_id:
            expenses.remove(expense)
    
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f)

def summary(args):
    expenses = load_expenses()
    year = args.year
    month = args.month
    total = 0

    table = PrettyTable()
    table.field_names = ['ID', 'Creation Date', 'Description', 'Amount']

    if month == None and year:
        for expense in expenses:
            if expense['year_creation'] == year:
                total += expense['amount']
                table.add_row([expense['id'], expense['creation_date'], expense['desc'], expense['amount']])
        print(table)
        print(f'Total amount for {year}: {total}')
    elif month and year == None:
        print('Please include the year')
    elif month and year:
        for expense in expenses:
            if expense['month_creation'] == month and expense['year_creation'] == year:
                total += expense['amount']
                table.add_row([expense['id'], expense['creation_date'], expense['desc'], expense['amount']])
        print(table)
        print(f'Total amount for {datetime.datetime(1, month, 1).strftime('%B')} of {year}: {total}')
    elif month == None and year == None:
        for expense in expenses:
            total += expense['amount']
            table.add_row([expense['id'], expense['creation_date'], expense['desc'], expense['amount']])
        print(table)
        print('Total of all expenses: ', total)

def list_expenses(args):
    expenses = load_expenses()

    table = PrettyTable()
    table.field_names = ['ID', 'Creation Date', 'Description', 'Amount']

    for expense in expenses:
        table.add_row([expense['id'], expense['creation_date'], expense['desc'], expense['amount']])

    print(table)

def update_expense(args):
    expenses = load_expenses()
    new_desc = args.desc
    new_amount = args.amount
    expense_id = args.id

    if new_desc and new_amount:
        for expense in expenses:
            if expense['id'] == expense_id:
                expense['desc'] = new_desc
                expense['amount'] = new_amount
    elif new_desc == None and new_amount:
        for expense in expenses:
            if expense['id'] == expense_id:
                expense['amount'] = new_amount
    elif new_desc and new_amount == None:
        for expense in expenses:
            if expense['id'] == expense_id:
                expense['desc'] = new_desc
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f)

def load_expenses():
    if not os.path.exists('expenses.json'):
        return []
    
    with open('expenses.json', 'r') as f:
        return json.load(f)
