import sys

from squiral import printout
from squiral import produce


def main_cli():
    printout(produce(int(sys.argv[-1])))
