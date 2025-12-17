import json
import datetime

def add_expense(args):
    print(args.amount, args.desc)

def delete_expense(args):
    print(args.id)

def summary(args):
    print(args.year, args.month)