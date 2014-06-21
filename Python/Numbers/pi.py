import sys
import math

MAX = 25

def main(howMany):
    """return up to nth decimal numbers from pi"""
    _format = '%.{0}f'.format(howMany)
    return _format

def validate_args(args):
    """docstring for validate_args"""
    if len(args) == 1 or len(args) > 2:
        return False, None
    return int(args[1]) <= MAX, int(args[1]) 

if __name__ == '__main__':
    valid, howMany = validate_args(sys.argv)
    if valid:
        _format = main(howMany)
        print _format % (math.pi)
    else:
        print 'Wrong number of arguments or provided argument exceeds max value.'
