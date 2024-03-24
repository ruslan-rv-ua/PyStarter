import argparse

def main():
    parser = argparse.ArgumentParser(description='Add two integers.')
    parser.add_argument('integer_1', type=int, help='The first integer')
    parser.add_argument('integer_2', type=int, help='The second integer')
    args = parser.parse_args()
    print(f'The sum of {args.integer_1} and {args.integer_2} is {args.integer_1+args.integer_2}')

if __name__ == "__main__":
    main()
