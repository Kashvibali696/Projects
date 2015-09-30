import sys
import math

MAX = 25


def main(howMany):
    """return up to nth decimal numbers from e"""
    return '%.{0}f'.format(howMany)


def validate_args(args):
    """docstring for validate_args"""
    if len(args) == 1 or len(args) > 2:
        return False, None
    return int(args[1]) <= MAX, int(args[1])


if __name__ == '__main__':
    valid, howMany = validate_args(sys.argv)
    if valid:
        _format = main(howMany)
        print _format % (math.e)
    else:
        print 'Wrong number of arguments or provided argument exceeds max value.'
