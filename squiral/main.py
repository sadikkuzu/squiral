from sys import argv

from squiral import printout
from squiral import produce


def main_cli():
    printout(produce(int(argv[-1])))
