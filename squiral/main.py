from sys import argv

from squiral import printout, produce

def main_cli():
    printout(produce(int(argv[-1])))
