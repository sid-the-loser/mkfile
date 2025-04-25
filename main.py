import argparse
import os

parser = argparse.ArgumentParser(prog="mkfile",
                                 description="A command that makes files.",
                                 epilog="Command made by SidTheLoser")

parser.add_argument('filename', 
                    help="name of the file you want to create")

args = parser.parse_args()

filename = args.filename

if not os.path.exists(filename):
    open(filename, "wb")
    print(os.path.abspath(filename), "created!")

else:
    print(os.path.abspath(filename), "already exists!") # create a custom error here

