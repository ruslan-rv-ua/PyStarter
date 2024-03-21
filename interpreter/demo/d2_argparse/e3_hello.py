import argparse

parser = argparse.ArgumentParser()
parser.add_argument ('--name', '-n', default='world')
args = parser.parse_args()
print(f'Hello {args.name}!')