import sys
import math

MAX = 25


class WrongNumberOfArguments(Exception):
    pass


def e_to_nth_digit(how_many):
    """return up to nth decimal numbers from e"""
    if how_many < 0 or how_many > MAX:
        how_many = MAX
    return '%.{0}f'.format(how_many) % (math.e, )


if __name__ == '__main__':
    if sys.args != 1:
        raise WrongNumberOfArguments('Number of arguments must be equal to one')
    print e_to_nth_digit(sys.argv)
