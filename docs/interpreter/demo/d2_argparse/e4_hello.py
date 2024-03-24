import argparse

def main():
    parser = argparse.ArgumentParser(description='Greet a user by name.')
    parser.add_argument('name', type=str, nargs='?', default='world',
                        help='the name of the user to greet (default: "world")')
    args = parser.parse_args()
    print(f'Hello, {args.name}!')

if __name__ == '__main__':
    main()
