import argparse


parser = argparse.ArgumentParser(
    prog = 'Test',
    description = 'Testing Git Hub Actions')
parser.add_argument('branch', help='Name of branch to work on')

args = parser.parse_args()
print("Hello world "+args.branch)

