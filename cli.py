import argparse
from expense_tracker import add_expense, delete_expense, summary, list_expenses, update_expense

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='action')

    add_parser = subparsers.add_parser('add')
    del_parser = subparsers.add_parser('del')
    summ_parser = subparsers.add_parser('summ')
    list_parser = subparsers.add_parser('list')
    update_parser = subparsers.add_parser('upd')

    add_parser.add_argument('amount', type=float)
    add_parser.add_argument('desc', type=str)
    add_parser.set_defaults(func=add_expense)

    del_parser.add_argument('id', type=int)
    del_parser.set_defaults(func=delete_expense)

    summ_parser.add_argument('-y','--year', type=int)
    summ_parser.add_argument('-m', '--month', type=int)
    summ_parser.set_defaults(func=summary)

    list_parser.set_defaults(func=list_expenses)

    update_parser.add_argument('id', type=int)
    update_parser.add_argument('-d', '--desc')
    update_parser.add_argument('-am', '--amount', type=float)
    update_parser.set_defaults(func=update_expense)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)

if __name__ == '__main__':
    main()