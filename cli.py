import argparse
from expense_tracker import add_expense, delete_expense, summary

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='action')

    add_parser = subparsers.add_parser('add')
    del_parser = subparsers.add_parser('del')
    summ_parser = subparsers.add_parser('summ')

    add_parser.add_argument('amount', type=float)
    add_parser.add_argument('desc', type=str)
    add_parser.set_defaults(func=add_expense)

    del_parser.add_argument('id', type=int)
    del_parser.set_defaults(func=delete_expense)

    summ_parser.add_argument('year', type=int)
    summ_parser.add_argument('-m', '--month', type=int)
    summ_parser.set_defaults(func=summary)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)

if __name__ == '__main__':
    main()