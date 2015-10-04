import sys


def fib(howMany):
    rv = []
    for i in xrange(howMany):
        if i == 0 or i == 1:
            rv.append(1)
        else:
            val = rv[i - 1] + rv[i - 2]
            rv.append(val)

    return rv


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1 or len(args) > 2:
        print 'Program needs 1 argument! Exiting!'
        sys.exit(1)
    try:
        howMany = int(args[1])
        if howMany > 0:
            result = fib(howMany)
            print result
        else:
            print 'No negative numbers or zero allowed!'
    except:
        print 'Wrong argument! Exiting!'
        sys.exit(2)
