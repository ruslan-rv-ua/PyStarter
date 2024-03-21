import argparse

parser = argparse.ArgumentParser()
parser.add_argument ('name', nargs='?', default='world')

args = parser.parse_args()
# print(args)

print(f'Hello {args.name}!')