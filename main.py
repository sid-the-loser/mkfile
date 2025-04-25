import argparse, os

version = "r1.0.0"

parser = argparse.ArgumentParser(prog="mkfile",
                                 description="A command that makes files.",
                                 epilog="Command made by sidtheloser")

parser.add_argument("-v", action="version", version="%(prog)s "+version)
parser.add_argument('filename', 
                    help="name of the file you want to create")
parser.add_argument("-o", "--ommit", action="store_true", help="ommits the absolute path being printed out into the command line")

args = parser.parse_args()

filename = args.filename
ommit_flag = args.ommit

if not os.path.exists(filename):
    open(filename, "wb")
    print(os.path.basename(filename) if ommit_flag else os.path.abspath(filename), "created!")

else:
    print(os.path.basename(filename) if ommit_flag else os.path.abspath(filename), "already exists!")
