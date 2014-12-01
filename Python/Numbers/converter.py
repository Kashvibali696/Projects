#!/usr/bin/env python


class WrongArgumentException(Exception):
    pass


def argument_validity(validity_func):
    def wrapper(func):
        def f(argument):
            if not validity_func(argument):
                raise WrongArgumentException
            return func(argument)
        return f
    return wrapper


def _is_bin_argument_valid(argument):
    bin_str = str(argument)
    f = lambda el: el in ['0', '1']
    return all(map(f, bin_str))


def _is_dec_argument_valid(argument):
    dec_str = str(argument)
    f = lambda el: el in map(str, range(0, 10))
    return all(map(f, dec_str))


@argument_validity(_is_bin_argument_valid)
def bin2dec(bin_number):
    ret, n_len = 0, len(str(bin_number))
    for index, el in enumerate(str(bin_number)):
        ret += (2 ** (n_len - index - 1)) * int(el)
    return ret


@argument_validity(_is_dec_argument_valid)
def dec2bin(decimal_number):
    dec_n = int(decimal_number)
    if dec_n in (0, 1):
		return str(dec_n)

    ret = ''
    while True:
        if dec_n == 1:
            ret = '1' + ret
            break
        remainder = dec_n % 2
        ret = str(remainder) + ret
        dec_n /= 2

    return ret